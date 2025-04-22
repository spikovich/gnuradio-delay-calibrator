import numpy as np
from gnuradio import gr
import pmt 

class blk(gr.sync_block):
    """
    Embedded Python Block to detect delay between two signals using cross-correlation
    and publish the result as a PMT message.
    """

    def __init__(self, buffer_size=1024, trigger_correlation=False):
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Delay Correaltion EPB',
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.buffer_size = int(buffer_size)
        self.message_port_register_out(pmt.intern('delay_lag'))

        self.buf0 = np.zeros(self.buffer_size, dtype=np.float32)
        self.buf1 = np.zeros(self.buffer_size, dtype=np.float32)
        self.ptr = 0
        self.correlation_done = False
        self.calibration_active = False

        self.tb = None

    def start_calibration(self):
        """Called to start calibration process."""
        print("EPB: Start Calibration Requested")
        self.ptr = 0
        self.correlation_done = False
        self.calibration_active = True

    def reset_calibration(self):
        """Called to reset calibration."""
        print("EPB: Reset Calibration Requested")
        self.calibration_active = False
        self.correlation_done = True

    def work(self, input_items, output_items):
        # Получаем входные данные
        data0 = input_items[0]
        data1 = input_items[1]
        # Определяем, сколько данных можем записать в буфер
        num_samples_to_process = len(data0)

        if self.calibration_active and not self.correlation_done:
            samples_to_copy = min(num_samples_to_process, self.buffer_size - self.ptr)

            if samples_to_copy > 0:
                self.buf0[self.ptr : self.ptr + samples_to_copy] = data0[:samples_to_copy]
                self.buf1[self.ptr : self.ptr + samples_to_copy] = data1[:samples_to_copy]
                self.ptr += samples_to_copy

            if self.ptr >= self.buffer_size:
                print(f"EPB: Buffer full ({self.ptr} samples). Performing correlation...")
                x0 = self.buf0 - np.mean(self.buf0)
                x1 = self.buf1 - np.mean(self.buf1)
                corr = np.correlate(x0, x1, mode='full')
                lag = int(np.argmax(corr) - (self.buffer_size - 1))
                print(f"EPB: Correlation complete. Calculated Lag = {lag}")
                self.message_port_pub(pmt.intern('delay_lag'), pmt.to_pmt(lag))
                self.correlation_done = True
                self.calibration_active = False
                print("EPB: Lag message published. Calibration cycle finished.")

        output_items[0][:num_samples_to_process] = 0.0

        return num_samples_to_process