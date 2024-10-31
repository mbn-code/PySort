from typing import List

# Initialize steps for visualization
steps = []

def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        # Get partition index and update visualization
        pivot_idx = partition(arr, low, high)
        # Recursively sort the left and right portions
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]  # Choose rightmost element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # Update visualization steps
        steps.append((arr.copy(), [j, high], [i+1]))  # Current comparison
        
        if arr[j] <= pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]
            # Record the swap in visualization
            steps.append((arr.copy(), [], [i, j]))

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps.append((arr.copy(), [], [i + 1, high]))
def update_quicksort(i: int, j: int) -> None:
    return i + 1

def update_quicksort(arr: List[int], i: int, j: int) -> None:
    """Update function for visualization"""
    global sort_info
    sort_info = {
        'comparing': [i, j],
        'swapping': []
    }