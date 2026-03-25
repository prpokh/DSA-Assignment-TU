import heapq

class MinHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []

    def push(self, val):
        """Adds an element to the heap while maintaining the heap property."""
        heapq.heappush(self.heap, val)
        print(f"Pushed {val}: {self.heap}")

    def pop(self):
        """Removes and returns the smallest element (the root)."""
        if self.heap:
            removed = heapq.heappop(self.heap)
            print(f"Popped {removed}: {self.heap}")
            return removed
        return "Heap is empty"

    def peek(self):
        """Returns the smallest element without removing it."""
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

# --- Example Usage ---
my_heap = MinHeap()

# Adding elements
my_heap.push(10)
my_heap.push(5)
my_heap.push(15)
my_heap.push(1)

print(f"\nSmallest element (peek): {my_heap.peek()}")

# Removing elements (will always be the smallest)
my_heap.pop()
my_heap.pop()