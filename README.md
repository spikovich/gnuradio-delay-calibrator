# GNU Radio Delay Calibrator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

The GNU Radio Delay Calibrator is a tool designed to automatically calibrate delay values for stream synchronization in GNU Radio flowgraphs. When working with multiple signals or sensor inputs in GNU Radio, precise timing synchronization is critical. This project provides an automated solution to find the optimal delay values needed for proper alignment of data streams.

## Features

- Automatic feedback control for stream calibration
- Python-based Out of Tree (OOT) block integration with GNU Radio
- Real-time delay adjustment for identical sample streams
- Options to start processing and reset calibration
- Stable operation for complex flowgraphs

## Project Structure

```
gnuradio-delay-calibrator/
├── blocks/                 # Custom GNU Radio blocks
│   └── epy_block_0_9fjxvh7m.py
├── docs/                   # Documentation
│   └── IPv6_Special_Assignments.pdf
├── examples/               # Example usage
│   ├── exampl.grc          # GNU Radio Companion example
│   ├── sa_epy_block_0.py   # Example embedded Python block
│   └── sa.py               # Example implementation
├── main/                   # Main application
│   └── main.grc            # Main GNU Radio Companion flowgraph
├── requirements.txt        # Project dependencies
├── LICENSE                 # MIT License
├── CODE_OF_CONDUCT.md      # Community guidelines
├── CONTRIBUTING.md         # Contributing guidelines
├── SECURITY.md             # Security policy
└── README.md               # This file
```

## Installation

1. Ensure GNU Radio is installed on your system
2. Clone this repository:
```bash
git clone https://github.com/yourusername/gnuradio-delay-calibrator.git
cd gnuradio-delay-calibrator
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Open the main GRC file in GNU Radio Companion:
```bash
gnuradio-companion main/main.grc
```
2. Execute the flowgraph to start the calibration process
3. The delay calibrator block will automatically adjust the delay parameters to achieve synchronization

4. Alternatively, you can run the Python script directly:
```bash
python3 main/sa.py
```

You can also check the examples directory for sample implementations and test cases.

## Requirements

- GNU Radio 3.10+
- Python 3.7+
- NumPy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
Before contributing, please read our [Code of Conduct](CODE_OF_CONDUCT.md) and [Contributing Guidelines](CONTRIBUTING.md).

## Security

For security issues, please review our [Security Policy](SECURITY.md) before reporting.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Last Updated

May 12, 2025