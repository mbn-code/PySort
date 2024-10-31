import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, Slider
import random
import matplotlib.animation as animation
import threading
import time
from typing import List, Callable

from includes.quick import quick_sort, update_quicksort
from includes.bubble import bubble_sort, update_bubblesort

def generate_random_data(size):
    return [random.randint(0, 100) for _ in range(size)]

def threaded_sort(sorting_algorithm, arr, update_callback, *args):
    start_time = time.time()
    sorting_algorithm(arr, *args)
    sort_info['time'] = time.time() - start_time
    update_callback(arr)

class SortVisualizer:
    def __init__(self):
        self.arr_size = 50
        self.is_random_data = True
        self.sorting_algorithm = quick_sort
        self.update_callback = update_quicksort
        self.args = [0, self.arr_size - 1]
        
        # Setup the main figure and subplots
        self.fig = plt.figure(figsize=(12, 8))
        self.ax = plt.subplot2grid((8, 1), (0, 0), rowspan=6)
        
        # Create button axes
        self.setup_buttons()
        
        self.reset_data()
        
        # Add speed control
        speed_ax = plt.axes([0.2, 0.15, 0.3, 0.02])
        self.speed_slider = Slider(speed_ax, 'Speed', 1, 100, valinit=50)
        
    def setup_buttons(self):
        # Algorithm selection buttons
        quick_btn_ax = plt.axes([0.2, 0.05, 0.15, 0.04])
        bubble_btn_ax = plt.axes([0.4, 0.05, 0.15, 0.04])
        self.quick_button = Button(quick_btn_ax, 'Quick Sort')
        self.bubble_button = Button(bubble_btn_ax, 'Bubble Sort')
        
        # Size input
        size_ax = plt.axes([0.2, 0.1, 0.15, 0.04])
        self.size_input = TextBox(size_ax, 'Size:', initial=str(self.arr_size))
        
        # Reset button
        reset_ax = plt.axes([0.4, 0.1, 0.15, 0.04])
        self.reset_button = Button(reset_ax, 'Reset Data')
        
        # Bind events
        self.quick_button.on_clicked(self.set_quicksort)
        self.bubble_button.on_clicked(self.set_bubblesort)
        self.size_input.on_submit(self.update_size)
        self.reset_button.on_clicked(self.reset_data)
        
    def set_quicksort(self, event):
        self.sorting_algorithm = quick_sort
        self.update_callback = update_quicksort
        self.args = [0, len(self.arr) - 1]
        self.reset_data()
        
    def set_bubblesort(self, event):
        self.sorting_algorithm = bubble_sort
        self.update_callback = update_bubblesort
        self.args = []
        self.reset_data()
        
    def update_size(self, text):
        try:
            self.arr_size = int(text)
            self.reset_data()
        except ValueError:
            pass
            
    def reset_data(self, event=None):
        global steps, sort_info, arr, sorted_arr
        steps = []
        sort_info = {}
        self.arr = generate_random_data(self.arr_size)
        arr = self.arr
        sorted_arr = self.arr.copy()
        
        if hasattr(self, 'ani'):
            self.ani.event_source.stop()
            
        self.sorting_thread = threading.Thread(
            target=threaded_sort,
            args=(self.sorting_algorithm, sorted_arr, self.update_callback, *self.args)
        )
        self.sorting_thread.start()
        
        self.ani = animation.FuncAnimation(
            self.fig, self.update_plot, frames=None, 
            interval=20, repeat=True, cache_frame_data=False)
            
    def update_plot(self, frame):
        if not steps:
            return
            
        # Batch process multiple steps
        batch_size = int(self.speed_slider.val)
        for _ in range(min(batch_size, len(steps))):
            current_arr, comparing, swapping = steps.pop(0)
            
        # Only clear axes once per batch
        self.ax.clear()
        bars = self.ax.bar(range(len(current_arr)), current_arr)
        
        # Bulk color update
        colors = ['lightblue'] * len(current_arr)
        for idx in comparing:
            colors[idx] = 'yellow'
        for idx in swapping:
            colors[idx] = 'red'
            
        for bar, color in zip(bars, colors):
            bar.set_color(color)
            
        self.ax.set_title(f"{self.sorting_algorithm.__name__}")
        
        # Reduce redraw frequency
        if frame % 2 == 0:
            plt.pause(0.001)

# Global variables needed for sorting
steps = []  # Now stores tuples of (array_state, comparing_indices, swapping_indices)
sort_info = {}
arr = []
sorted_arr = []

# Create and show visualizer
visualizer = SortVisualizer()
plt.show()