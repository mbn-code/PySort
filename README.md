# PySort

Python Sorting Visualized.

## Sorting Algorithm Visualization

This repository contains a Python script that visualizes various sorting algorithms using `matplotlib` to create an animated visualization of the sorting process.

## Usage

1. Ensure you have Python and required dependencies installed:

    ```bash
    pip install matplotlib
    ```

2. Run `src/main.py`
3. Use the interactive interface to:
   - Select sorting algorithms using buttons
   - Adjust array size using the input box
   - Control animation speed using the slider
   - Reset data with the reset button

## Supported Sorting Algorithms

Currently implemented:

- QuickSort (O(n log n) average case)
- BubbleSort (O(n²))

## Visualization Features

- Interactive GUI with matplotlib
- Real-time animation of sorting process
- Color-coded visualization:
  - Yellow: Elements being compared
  - Red: Elements being swapped
  - Light blue: Unsorted elements
- Adjustable animation speed via slider
- Customizable array size
- Reset functionality to generate new random data

## Project Structure

```bash
src/
├── main.py           # Main visualization interface
└── includes/         # Sorting algorithm implementations
    ├── quick.py      # QuickSort implementation
    └── bubble.py     # BubbleSort implementation
```
