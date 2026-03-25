def insertion_sort(arr):
    # Start from the second element (index 1) as the first is "sorted"
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct location
        arr[j + 1] = key

# Example usage:
data = [12, 11, 13, 5, 6]
insertion_sort(data)
print("Sorted array:", data)