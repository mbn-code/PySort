from typing import List

steps = []

def bubble_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            # Visualize comparison
            steps.append((arr.copy(), [j, j+1], []))
            
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Visualize swap
                steps.append((arr.copy(), [], [j, j+1]))
                swapped = True
                
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    # Final state
    steps.append((arr.copy(), [], []))

def update_bubblesort(arr: List[int]) -> None:
    """Update function for visualization"""
    global sort_info
    sort_info = {
        'array': arr.copy(),
        'comparing': [],
        'swapping': []
    }