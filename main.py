import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
import threading
import time

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i, j = low - 1, high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort_helper(arr, low, high, callback):
    if low < high:
        pivot_index = partition(arr, low, high)
        # Call the callback to update the animation
        callback(arr[:], low, high, pivot_index)
        quick_sort_helper(arr, low, pivot_index, callback)
        quick_sort_helper(arr, pivot_index + 1, high, callback)

def bubble_sort_helper(arr, callback):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            callback(arr[:])

def update_quicksort(current_arr, low, high, pivot_index):
    global steps
    steps.append(current_arr[:])

def update_bubblesort(current_arr):
    global steps
    steps.append(current_arr[:])

def generate_random_data(size):
    return [random.randint(1, 150) for _ in range(size)]

arr_size = 299  # Change the size of the dataset here
arr = generate_random_data(arr_size)
original_data = arr.copy()
steps = []
sorted_arr = arr.copy()

sorting_algorithm = quick_sort  # Start with QuickSort
start_time = None
is_random_data = True  # Set to True if data is initially random, False if pre-sorted

fig, ax = plt.subplots()

def threaded_sort(sorting_func):
    global sorted_arr, start_time
    start_time = time.time()
    if sorting_func == quick_sort:
        quick_sort_helper(sorted_arr, 0, len(sorted_arr) - 1, update_quicksort)
    elif sorting_func == bubble_sort:
        bubble_sort_helper(sorted_arr, update_bubblesort)
    end_time = time.time()

# Use threading to perform sorting in the background
sorting_thread = threading.Thread(target=threaded_sort, args=(sorting_algorithm,))
sorting_thread.start()

def update_plot(frame):
    global sorting_algorithm
    if frame < len(steps):
        ax.clear()
        ax.set_title(f"Sorting - {sorting_algorithm.__name__} - Pass {frame + 1} | "
                     f"Time taken: {time.time() - start_time:.5f} seconds | "
                     f"Random Data: {is_random_data} | Data Amount: {arr_size}")
        padded_steps = steps[frame] + [0] * (len(arr) - len(steps[frame]))
        ax.bar(range(len(arr)), padded_steps, color='lightblue')  # Plot bars for each step
    else:
        ax.clear()
        ax.set_title(f"Sorting - {sorting_algorithm.__name__} - Completed | "
                     f"Time taken: {time.time() - start_time:.5f} seconds | "
                     f"Random Data: {is_random_data} | Data Amount: {arr_size}")
        ax.bar(range(len(arr)), sorted_arr, color='lightgreen')  # Plot the final sorted bars

ani = animation.FuncAnimation(fig, update_plot, frames=len(steps) + 1, interval=10, repeat=False)  # Adjust the interval as needed
plt.show()
