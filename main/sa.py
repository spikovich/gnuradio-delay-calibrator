#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
import numpy
from gnuradio import blocks, gr
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sa_epy_block_0 as epy_block_0  # embedded python block
import sip


def snipfcn_snippet_0(self):
    if hasattr(self, 'epy_block_0') and hasattr(self.epy_block_0, 'set_parent_flowgraph_reference'):
        print("PYTHON SNIPPET: Attempting to set parent for epy_block_0")
        self.epy_block_0.set_parent_flowgraph_reference(self)
    else:
        print("PYTHON SNIPPET ERROR: epy_block_0 or set_parent_flowgraph_reference not found.")


def snippets_main_after_init(tb):
    snipfcn_snippet_0(tb)

class sa(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "sa")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.start_calibration_button = start_calibration_button = False
        self.samp_rate = samp_rate = 32000
        self.reset_calibration_button = reset_calibration_button = False
        self.compensation_delay = compensation_delay = 0

        ##################################################
        # Blocks
        ##################################################

        _start_calibration_button_push_button = Qt.QPushButton('Start Calibration')
        _start_calibration_button_push_button = Qt.QPushButton('Start Calibration')
        self._start_calibration_button_choices = {'Pressed': 1, 'Released': 0}
        _start_calibration_button_push_button.pressed.connect(lambda: self.set_start_calibration_button(self._start_calibration_button_choices['Pressed']))
        _start_calibration_button_push_button.released.connect(lambda: self.set_start_calibration_button(self._start_calibration_button_choices['Released']))
        self.top_layout.addWidget(_start_calibration_button_push_button)
        _reset_calibration_button_push_button = Qt.QPushButton('Reset Calibration')
        _reset_calibration_button_push_button = Qt.QPushButton('Reset Calibration')
        self._reset_calibration_button_choices = {'Pressed': 1, 'Released': 0}
        _reset_calibration_button_push_button.pressed.connect(lambda: self.set_reset_calibration_button(self._reset_calibration_button_choices['Pressed']))
        _reset_calibration_button_push_button.released.connect(lambda: self.set_reset_calibration_button(self._reset_calibration_button_choices['Released']))
        self.top_layout.addWidget(_reset_calibration_button_push_button)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            200, #size
            samp_rate, #samp_rate
            'Source signals', #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['red', 'blue', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            200, #size
            samp_rate, #samp_rate
            'Calibrated signal', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['red', 'green', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.epy_block_0 = epy_block_0.blk(buffer_size=4096)
        self.blocks_throttle2_0_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(0.1) * samp_rate) if "time" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(0.1) * samp_rate) if "time" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(0.1) * samp_rate) if "time" == "time" else int(0.1), 1) )
        self.blocks_message_debug_0 = blocks.message_debug(True, gr.log_levels.info)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_char*1, compensation_delay)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_char*1, 5)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 256, 8129))), True)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.epy_block_0, 'calculated_lag'), (self.blocks_message_debug_0, 'print'))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.blocks_throttle2_0_1, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.epy_block_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_throttle2_0_1, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.epy_block_0, 0), (self.blocks_throttle2_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sa")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_start_calibration_button(self):
        return self.start_calibration_button

    def set_start_calibration_button(self, start_calibration_button):
        self.start_calibration_button = start_calibration_button

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_1.set_sample_rate(self.samp_rate)

    def get_reset_calibration_button(self):
        return self.reset_calibration_button

    def set_reset_calibration_button(self, reset_calibration_button):
        self.reset_calibration_button = reset_calibration_button

    def get_compensation_delay(self):
        return self.compensation_delay

    def set_compensation_delay(self, compensation_delay):
        self.compensation_delay = compensation_delay
        self.blocks_delay_1.set_dly(int(self.compensation_delay))




def main(top_block_cls=sa, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    snippets_main_after_init(tb)
    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
