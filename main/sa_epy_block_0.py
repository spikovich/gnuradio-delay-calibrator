import numpy as np
from gnuradio import gr
import pmt

class blk(gr.sync_block):
    # Добавляем top_block_instance=None в параметры __init__
    def __init__(self, buffer_size=1024): # <--- ИЗМЕНЕНИЕ
        gr.sync_block.__init__(
            self,
            name='Delay Auto-Corrector EPB',
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.buffer_size = int(buffer_size)
        self.message_port_register_out(pmt.intern('calculated_lag'))

        self.buf0 = np.array([], dtype=np.float32)
        self.buf1 = np.array([], dtype=np.float32)

        self.calibration_active = False
        self.correlation_done_this_cycle = True
        
        # Сохраняем переданную ссылку
        self.parent_flowgraph_ref = None  # <--- ИЗМЕНЕНИЕ
        #if self.parent_flowgraph_ref is not None:
            #print("EPB INFO: parent_flowgraph_ref received via __init__.")
        #else:
            # Это сообщение теперь будет более критичным, если не сработает ручная установка
           # print("EPB CRITICAL WARNING: parent_flowgraph_ref NOT received via __init__ OR manual set. Interaction will fail.")

        self.last_start_button_var_val = False
        self.last_reset_button_var_val = False

        self.start_button_variable_id = "start_calibration_button"
        self.reset_button_variable_id = "reset_calibration_button"
        
        self.initial_compensation_delay_set_on_start = False
        self.work_call_count = 0 

        print(f"EPB Initialized: Buffer Size = {self.buffer_size}")
        #if self.parent_flowgraph_ref is None:
            #print("EPB INFO: __init__ - parent_flowgraph_ref is initially None. Manual set in top_block is expected.")

    # Метод _try_get_parent_flowgraph() УДАЛЕН
    def set_parent_flowgraph_reference(self, parent_ref):
        #print(f"EPB DEBUG: set_parent_flowgraph_reference called with parent_ref type: {type(parent_ref)}")
        self.parent_flowgraph_ref = parent_ref
        #if self.parent_flowgraph_ref is not None:
            #print("EPB INFO: parent_flowgraph_ref successfully set via method call.")
        #else:
            #print("EPB WARNING: parent_flowgraph_ref is STILL None after method call set_parent_flowgraph_reference.")

    def _check_buttons(self):
        # print("EPB DEBUG: _check_buttons() called.")
        parent_fg = self.parent_flowgraph_ref # Теперь используем напрямую
        if parent_fg is None:
            # print("EPB DEBUG: _check_buttons() - parent_fg_ref is None, returning.")
            return 
        # ... остальной код _check_buttons без изменений ...
        try:
            getter_start_name = f"get_{self.start_button_variable_id}"
            if hasattr(parent_fg, getter_start_name):
                current_start_button_var_bool = getattr(parent_fg, getter_start_name)() 
                if current_start_button_var_bool and not self.last_start_button_var_val:
                    self.start_calibration()
                self.last_start_button_var_val = current_start_button_var_bool
            #else: 
                # print(f"EPB DEBUG: _check_buttons() - Start button getter '{getter_start_name}' not found.") 
        except Exception as e:
            print(f"EPB Error checking start button variable: {e}")

        try:
            getter_reset_name = f"get_{self.reset_button_variable_id}"
            if hasattr(parent_fg, getter_reset_name):
                current_reset_button_var_bool = getattr(parent_fg, getter_reset_name)()
                if current_reset_button_var_bool and not self.last_reset_button_var_val:
                    self.reset_calibration()
                self.last_reset_button_var_val = current_reset_button_var_bool
            #else: 
              #  print(f"EPB DEBUG: _check_buttons() - Reset button getter '{getter_reset_name}' not found.") 
        except Exception as e:
            print(f"EPB Error checking reset button variable: {e}")


    def _set_compensation_delay_on_parent(self, delay_value):
        parent_fg = self.parent_flowgraph_ref
        if parent_fg is None:
            print("EPB Warning: Cannot set compensation_delay, parent_flowgraph_ref is None.")
            return False
        # ... остальной код _set_compensation_delay_on_parent без изменений ...
        try:
            comp_delay_var_name = 'compensation_delay'
            setter_method_name = f"set_{comp_delay_var_name}"
            if hasattr(parent_fg, setter_method_name):
                #print(f"EPB DEBUG: Setting compensation_delay to {int(round(delay_value))}") 
                getattr(parent_fg, setter_method_name)(int(round(max(0,delay_value)))) 
                return True
            else:
                print(f"EPB Error: Parent flowgraph does not have method {setter_method_name}()")
                return False
        except Exception as e:
            print(f"EPB Error: Could not set {comp_delay_var_name} on parent: {e}")
            return False
            
    def _get_compensation_delay_from_parent(self):
        parent_fg = self.parent_flowgraph_ref
        if parent_fg is None:
            #print("EPB DEBUG: _get_compensation_delay_from_parent() - parent_fg_ref is None. Returning 0.")
            return 0 
        # ... остальной код _get_compensation_delay_from_parent без изменений ...
        try:
            comp_delay_var_name = 'compensation_delay'
            getter_method_name = f"get_{comp_delay_var_name}"
            if hasattr(parent_fg, getter_method_name):
                val = getattr(parent_fg, getter_method_name)()
                #print(f"EPB DEBUG: Got compensation_delay = {val}") 
                return val
            else:
                print(f"EPB Error: Parent flowgraph does not have method {getter_method_name}(). Returning 0.")
                return 0
        except Exception as e:
            print(f"EPB Error: Could not get {comp_delay_var_name} from parent: {e}. Returning 0.")
            return 0

    def start_calibration(self):
        print("EPB: Start Calibration Action Triggered")
        self.calibration_active = True
        self.correlation_done_this_cycle = False
        self.buf0 = np.array([], dtype=np.float32)
        self.buf1 = np.array([], dtype=np.float32)
        print("EPB: Buffers cleared, awaiting data for correlation.")

    def reset_calibration(self):
        print("EPB: Reset Calibration Action Triggered")
        self.calibration_active = False
        self.correlation_done_this_cycle = True
        self.buf0 = np.array([], dtype=np.float32)
        self.buf1 = np.array([], dtype=np.float32)

        if self._set_compensation_delay_on_parent(0):
            print(f"EPB: Compensation_delay reset to 0.")
            self.initial_compensation_delay_set_on_start = True 
        else:
            print(f"EPB Warning: Failed to reset compensation_delay to 0.")
        print("EPB: Calibration reset logic complete.")

    def work(self, input_items, output_items):
        self.work_call_count += 1
        # Убрали вызов _try_get_parent_flowgraph() отсюда, т.к. ссылка должна быть установлена в __init__ (вручную)

        if self.parent_flowgraph_ref is not None: # Проверяем, была ли ссылка установлена
            # print(f"EPB DEBUG: work() call #{self.work_call_count}, parent_flowgraph_ref IS available.")
            if not self.initial_compensation_delay_set_on_start:
                self.reset_calibration() 
            self._check_buttons()
        else:
            # Это будет происходить, если ручная установка self.parent_flowgraph_ref в sa.py не сработала
            if self.work_call_count < 5: # Печатаем только первые несколько раз, чтобы не засорять
                print(f"EPB WARNING: work() call #{self.work_call_count} - parent_flowgraph_ref is STILL None. Interaction with GUI/variables will fail.")
        
        if not (input_items and \
                len(input_items) >= 2 and \
                input_items[0] is not None and \
                input_items[1] is not None and \
                len(input_items[0]) > 0 and \
                len(input_items[1]) > 0):
            if output_items and output_items[0] is not None:
                 output_items[0][:] = 0.0 
            return 0
        
        self.buf0 = np.concatenate((self.buf0, input_items[0]))
        self.buf1 = np.concatenate((self.buf1, input_items[1]))

        max_buf_len = self.buffer_size * 2 
        if len(self.buf0) > max_buf_len: self.buf0 = self.buf0[-max_buf_len:]
        if len(self.buf1) > max_buf_len: self.buf1 = self.buf1[-max_buf_len:]

        if self.calibration_active and not self.correlation_done_this_cycle:
            if len(self.buf0) >= self.buffer_size and len(self.buf1) >= self.buffer_size:
                if self.parent_flowgraph_ref is None: # Еще одна проверка перед использованием
                    print("EPB CRITICAL ERROR: parent_flowgraph_ref is None before correlation. Aborting calibration cycle.")
                    self.calibration_active = False 
                    if output_items and output_items[0] is not None: output_items[0][:] = input_items[0]
                    return len(input_items[0])

                print(f"EPB: Buffers filled. Performing correlation...")
                # ... остальной код корреляции ...
                sig0, sig1 = self.buf0[-self.buffer_size:], self.buf1[-self.buffer_size:]
                proc_sig0, proc_sig1 = sig0 - np.mean(sig0), sig1 - np.mean(sig1)
                corr = np.correlate(proc_sig0, proc_sig1, mode='full')
                lag_at_max = np.argmax(corr) - (self.buffer_size - 1)

                print(f"EPB: Correlation complete. Lag = {lag_at_max}")
                self.message_port_pub(pmt.intern('calculated_lag'), pmt.to_pmt(float(lag_at_max)))

                current_delay_val = self._get_compensation_delay_from_parent()
                new_delay = current_delay_val + lag_at_max
                
                self._set_compensation_delay_on_parent(new_delay)
                
                self.correlation_done_this_cycle = True
                self.calibration_active = False
                print("EPB: Calibration cycle finished.")
                self.buf0, self.buf1 = np.array([], dtype=np.float32), np.array([], dtype=np.float32)

        if output_items and output_items[0] is not None:
            output_len = len(output_items[0])
            input_len = len(input_items[0])
            copy_len = min(output_len, input_len)
            output_items[0][:copy_len] = input_items[0][:copy_len]
            if output_len > copy_len:
                output_items[0][copy_len:] = 0.0
        
        return len(input_items[0])