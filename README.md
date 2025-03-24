# gnuradio-delay-calibrator

## Description of the Solution

This project implements an automatic feedback control to find the correct delay value for stream calibration in a GNU Radio flowgraph. The solution involves creating a Python-based Out of Tree (OOT) block that handles the automatic feedback control for stream calibration. The block is integrated into the flowgraph and automatically adjusts the delay value to ensure the stream of identical samples is corrected. The block includes options to start processing and reset for new calibration, ensuring stability and usability in more complicated use cases.