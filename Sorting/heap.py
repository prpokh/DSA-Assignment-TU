import heapq

def heap_sort_simple(arr):
    # 1. Create a min-heap from the array
    heapq.heapify(arr)
    
    # 2. Pop elements one by one to get them in sorted order
    # Note: This returns a new list; heapq.heapify modifies the list in-place
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Alternative: In-place sort (ascending)
def heap_sort_inplace(arr):
    # heapq doesn't have a direct "heap_sort" function, 
    # but we can simulate it:
    h = []
    for value in arr:
        heapq.heappush(h, value)
    
    for i in range(len(arr)):
        arr[i] = heapq.heappop(h)

# Example usage:
data = [12, 11, 13, 5, 6, 7]
sorted_data = heap_sort_simple(data)
print("Sorted array:", sorted_data)