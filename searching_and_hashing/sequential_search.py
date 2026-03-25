def sequential_search(data_list, target):
    for index in range(len(data_list)):
        if data_list[index] == target:
            return index  # Match found, return the position
            
    return -1  # End of list reached without finding the target

# Example Usage:
numbers = [10, 23, 45, 70, 11, 15]
search_item = 70

result = sequential_search(numbers, search_item)

if result != -1:
    print(f"Element {search_item} found at index {result}.")
else:
    print(f"Element {search_item} not found in the list.")