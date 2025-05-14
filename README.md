
# GNU Radio Delay Calibrator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

The GNU Radio Delay Calibrator is a tool designed to automatically determine and compensate for delay differences between two data streams within a GNU Radio flowgraph. Precise timing synchronization is critical when working with multiple signals. This project provides an automated solution using an Embedded Python Block (EPB) that performs cross-correlation to find the optimal delay value needed for proper alignment of identical sample streams.

## Features

- Automatic feedback control for stream delay calibration.
- Custom signal processing logic implemented within an Embedded Python Block (EPB).
- GUI controls to initiate calibration and reset the compensation.
- Real-time observation of signal alignment.
- Difference signal output for precise alignment verification.
- Designed to work seamlessly when launched from GNU Radio Companion.

## Project Structure
```
gnuradio-delay-calibrator/
├── blocks/                 # Custom GNU Radio blocks
│   └── epy_block_0_9fjxvh7m.py
├── docs/                   # Documentation
│   ├── Automatic Stream Delay Calibration in GNU Radio by Spika.pdf
│   └── IPv6SpecialAssignments25 (pdf.io).pdf
├── examples/               # Example usage
│   ├── exampl.grc          # GNU Radio Companion example
│   ├── sa_epy_block_0.py   # Example embedded Python block
│   └── sa.py               # Example implementation
├── main/                   # Main application
│   ├── main.grc            # Main GNU Radio Companion flowgraph
│   ├── sa_epy_block_0.py   # Main embedded Python block implementation
│   └── sa.py               # Generated Python script
├── requirements.txt        # Project dependencies
├── LICENSE                 # MIT License
├── CODE_OF_CONDUCT.md      # Community guidelines
├── CONTRIBUTING.md         # Contributing guidelines
├── SECURITY.md             # Security policy
└── README.md               # This file
```
## Prerequisites

1.  **GNU Radio:** Version 3.9.0 or newer installed.
    *   Ensure `gnuradio-companion` is operational and your Python 3 environment is correctly configured for GNU Radio.
    *   Standard components like `gr-blocks`, `gr-qtgui`, and `gr-analog` are required.
2.  **Python Dependencies:**
    *   NumPy 1.25.0 or newer (may be installed with GNU Radio)
    *   PyQt5 (typically installed with GNU Radio for `gr-qtgui`)
    *   These are listed in `requirements.txt` for completeness.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/spikovich/gnuradio-delay-calibrator.git
    cd gnuradio-delay-calibrator
    ```
    

2.  **(Optional) Install Dependencies if needed:**
    If you have a very minimal Python setup or use a virtual environment without system site-packages, you might need to install dependencies:
    ```bash
    # Activate your virtual environment if you use one
    # pip install -r requirements.txt
    ```
    Usually, a standard GNU Radio installation provides the necessary Python packages.

## Usage and Verification

The primary method to run and test this project is via GNU Radio Companion (GRC).

1.  **Open the Flowgraph in GRC:**
    Navigate to the `main` directory and open the GRC file:
    ```bash
    cd main 
    gnuradio-companion main.grc
    ```

2.  **Verify Key Components in GRC (Important for Evaluation):**    *   **Embedded Python Block (EPB) - "Delay Auto-Corrector & Difference EPB":**
        *   Double-click this block in the GRC canvas.
        *   Go to the 'Source Code' tab (or 'Properties' depending on GRC version).
        *   The Python code for the block is embedded here. A reference copy of this code is also in `main/sa_epy_block_0.py`. **Ensure the code within GRC matches this reference file.**
        *   Key parameters to check: `Buffer_Size` (e.g., 4096).

    *   **Python Snippet Block (ID: `snippet_0`):**
        *   This block is crucial for enabling the EPB to interact with the main flowgraph variables.
        *   Double-click the "snippet_0" block.
        *   In its properties, check the `Init Code` (which runs under `Section: main_after_init`). It should contain:
            ```python
            # self here refers to the top_block instance (e.g., 'sa')
            # epy_block_0 is the ID of the Embedded Python Block
            if hasattr(self, 'epy_block_0') and hasattr(self.epy_block_0, 'set_parent_flowgraph_reference'):
                # print("PYTHON SNIPPET: Attempting to set parent for epy_block_0") # Debug, can be commented
                self.epy_block_0.set_parent_flowgraph_reference(self)
            # else:
                # print("PYTHON SNIPPET ERROR: epy_block_0 or its method not found.") # Debug, can be commented
            ```
            (Ensure `epy_block_0` in the snippet code matches the actual ID of your "Delay Auto-Corrector EPB" block in GRC.)

    *   **Variables:**
        *   `compensation_delay`: Check its default value (e.g., set to `2` for clear demonstration, though the EPB will reset it to `0` on startup).
        *   `System Delay` (in the first `Delay` block): Ensure it's set to the desired value (e.g., `5`).

3.  **Generate and Execute the Flowgraph:**
    *   In GRC, click the "Generate flowgraph" button (gear icon).
    *   Then, click the "Execute the flowgraph" button (play icon ▶).

4.  **Interacting with the Calibrator GUI:**
    *   A GUI window will appear with "Start Calibration" and "Reset Calibration" buttons, and a Time Sink display.    *   **Time Sink (with 2 inputs):** This graph shows:
        *   Signal 1 (e.g., red): The reference signal with the fixed system delay.
        *   Signal 2 (e.g., green): The signal whose delay is being compensated.
    *   **Difference Output:** The block also outputs the difference between the reference and compensated signals, which can be visualized in a separate sink to verify alignment quality.
    *   **Initial State:** Upon startup, the `compensation_delay` for Signal 2 is reset to `0` by the EPB. You should observe that Signal 1 and Signal 2 are out of sync.
    *   **"Start Calibration" Button:**
        *   Click this button to initiate one automatic delay calibration cycle.
        *   **Console Output (in GRC's bottom panel):** Look for messages like:            ```
            EPB: Start Calibration Action Triggered
            ...
            Auto-Compensation: Calculated lag = <X>
            Auto-Compensation: New compensation delay = <Y> 
            ```
            The `Message Debug` block (if enabled and connected) will also show the calculated `lag (X)`.
        *   **Time Sink Display:** After a successful calibration, Signal 1 and Signal 2 should **perfectly overlap**, appearing as a single trace. The value of Y should equal the system delay.
    *   **"Reset Calibration" Button:**
        *   Click this to set the `compensation_delay` back to `0`.
        *   The signals on the Time Sink will become unsynchronized again.
    *   **Stability Test:** After a successful calibration (signals overlap), wait a few seconds and press "Start Calibration" again. The calculated `Lag` should be `0` (or very close), and the `compensation_delay` should remain unchanged.

## Output to Console

When calibration is triggered, the EPB will print:
- The calculated `lag` between the two signal paths.
- The new `compensation_delay` value that has been set.

Example:
```
Auto-Compensation: Calculated lag = 5
Auto-Compensation: New compensation delay = 5
```
## Requirements Summary

- GNU Radio 3.9.0 or newer
- Python 3.x (as required by GNU Radio)
- NumPy 1.25.0 or newer

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) and our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Security

Please refer to our [SECURITY.md](SECURITY.md) for reporting security concerns.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Last Updated

May 14, 2025