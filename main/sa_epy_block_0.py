import numpy as np
from gnuradio import gr
import pmt 

class blk(gr.sync_block):
    """
    Embedded Python Block to detect delay between two signals using cross-correlation
    and publish the result as a PMT message.
    """

    def __init__(self, buffer_size=1024): # Добавляем параметр buffer_size и флаг для запуска
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Delay Correaltion EPB', # Более осмысленное имя
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32] # Оставляем выход для совместимости с sync_block, будем писать нули
        )
        # Регистрация параметров
        self.buffer_size = int(buffer_size) # Убедимся, что целое
        # Регистрация порта для выходных сообщений
        self.message_port_register_out(pmt.intern('delay_lag')) # Дадим более конкретное имя порту

        # Инициализация внутренних переменных
        self.buf0 = np.zeros(self.buffer_size, dtype=np.float32)
        self.buf1 = np.zeros(self.buffer_size, dtype=np.float32)
        self.ptr = 0
        self.correlation_done = False # Флаг, что корреляция выполнена
        self.calibration_active = False # Флаг, что калибровка запущена

        # Ссылка на top_block (нужна для управления кнопками/переменными напрямую, если решим)
        self.tb = None # Будет установлена извне

    # --- Добавляем методы для управления извне (например, через кнопки) ---

    def start_calibration(self):
        """Вызывается для начала процесса калибровки."""
        print("EPB: Start Calibration Requested")
        self.ptr = 0 # Сброс указателя буфера
        self.correlation_done = False # Разрешаем новую корреляцию
        self.calibration_active = True # Активируем калибровку

    def reset_calibration(self):
        """Вызывается для сброса калибровки."""
        print("EPB: Reset Calibration Requested")
        self.calibration_active = False
        self.correlation_done = True # Предотвращаем корреляцию до нового старта
        # Сброс задержки должен происходить вне этого блока, в GRC или callback'е

    # --- Основной метод work ---

    def work(self, input_items, output_items):
        # Получаем входные данные
        data0 = input_items[0]
        data1 = input_items[1]
        # Определяем, сколько данных можем записать в буфер
        num_samples_to_process = len(data0) # Сколько данных пришло на вход

        if self.calibration_active and not self.correlation_done:
            samples_to_copy = min(num_samples_to_process, self.buffer_size - self.ptr)

            if samples_to_copy > 0:
                self.buf0[self.ptr : self.ptr + samples_to_copy] = data0[:samples_to_copy]
                self.buf1[self.ptr : self.ptr + samples_to_copy] = data1[:samples_to_copy]
                self.ptr += samples_to_copy

            # Если буфер заполнен и калибровка активна
            if self.ptr >= self.buffer_size:
                print(f"EPB: Buffer full ({self.ptr} samples). Performing correlation...")
                # Убираем среднее
                x0 = self.buf0 - np.mean(self.buf0)
                x1 = self.buf1 - np.mean(self.buf1)
                # Считаем корреляцию
                corr = np.correlate(x0, x1, mode='full')
                # Находим лаг
                lag = int(np.argmax(corr) - (self.buffer_size - 1))
                print(f"EPB: Correlation complete. Calculated Lag = {lag}")
                # Публикуем результат
                self.message_port_pub(pmt.intern('delay_lag'), pmt.to_pmt(lag))
                # Отмечаем, что корреляция завершена (для этого цикла калибровки)
                self.correlation_done = True
                self.calibration_active = False # Опционально: остановить калибровку после одного расчета
                print("EPB: Lag message published. Calibration cycle finished.")

        # Заполняем выходной буфер нулями (т.к. sync_block требует выходных данных)
        output_items[0][:num_samples_to_process] = 0.0

        # Возвращаем количество обработанных (и произведенных) сэмплов
        return num_samples_to_process