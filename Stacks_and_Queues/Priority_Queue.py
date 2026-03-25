class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        # Pre-allocate the fixed-size "array"
        self.queue = [None] * capacity 
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data, priority):
        if self.is_full():
            print("Queue Overflow")
            return

        new_item = {'data': data, 'priority': priority}

        # If empty, just place at the start
        if self.is_empty():
            self.queue[0] = new_item
            self.size += 1
        else:
            # Start from the back and shift elements to the right
            # to make room for the new item (Sorted Insertion)
            i = self.size - 1
            while i >= 0 and self.queue[i]['priority'] < priority:
                self.queue[i + 1] = self.queue[i]
                i -= 1
            
            # Place the new item in its sorted position
            self.queue[i + 1] = new_item
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        
        # In a sorted array, the highest priority is always at index 0
        highest = self.queue[0]
        
        # Shift everything left to fill the gap
        for i in range(self.size - 1):
            self.queue[i] = self.queue[i + 1]
        
        self.queue[self.size - 1] = None # Clean up
        self.size -= 1
        return highest

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
# Example usage
if __name__ == "__main__":
    pq = PriorityQueue(5)
    
    pq.enqueue("Task 1", priority=2)
    pq.enqueue("Task 2", priority=5)
    pq.enqueue("Task 3", priority=1)
    
    print("Highest Priority Task:", pq.peek())  # Task 2
    
    print("Dequeue:", pq.dequeue())  # Task 2
    print("Next Highest Priority Task:", pq.peek())  # Task 1