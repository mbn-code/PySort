# PySort
Python Sorting Visualised. 

# Sorting Algorithm Visualization

This repository contains a Python script that visualizes two sorting algorithms: QuickSort and BubbleSort. The script uses `matplotlib` to create an animated visualization of the sorting process.

## Usage

1. Make sure you have Python and `matplotlib` installed.

2. Copy the code from the `main.py` file into your Python environment or IDE.

3. Run the script. It will generate random data of a specified size and then sort it using the chosen algorithm (QuickSort by default).

4. The animated visualization will show the sorting process step by step.

5. The final sorted array will be displayed once the sorting process is complete.

## Sorting Algorithms

### QuickSort

QuickSort is a popular divide-and-conquer sorting algorithm. It partitions the input array into smaller subarrays and then recursively sorts each subarray. It has an average time complexity of O(n log n) and is often faster than other sorting algorithms for large datasets.

### BubbleSort

BubbleSort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. It has a time complexity of O(n^2) and is not efficient for large datasets.

## Visualization

The visualization uses `matplotlib.animation` to display the sorting process in real-time. The bars in the plot represent the elements of the array, and their positions change as the sorting algorithm rearranges the elements.

## Configuration

You can customize the behavior of the script by modifying the following variables:

- `arr_size`: Change the size of the dataset here.

- `sorting_algorithm`: Set to `quick_sort` for QuickSort or `bubble_sort` for BubbleSort.

- `is_random_data`: Set to `True` if data is initially random, `False` if pre-sorted.

- `interval`: Adjust the interval (in milliseconds) between animation frames. Increase for slower animation, decrease for faster animation.

## Contribution

Contributions to this repository are welcome. If you find any issues or have improvements to suggest, feel free to open a pull request or an issue.

## Credits

The visualization code is inspired by online tutorials and examples. The sorting algorithms are implemented based on well-known algorithms.

## License

This project is licensed under the [MIT License](LICENSE).
