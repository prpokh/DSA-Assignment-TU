import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # Helps maintain order for items with identical priority

    def push(self, item, priority):
        """
        Inserts an item with a given priority.
        We include self._index to handle cases where two items have the 
        same priority, ensuring they are returned in the order they were added.
        """
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
        print(f"Added '{item}' with priority {priority}")

    def pop(self):
        """Removes and returns the item with the highest priority (lowest value)."""
        if not self._queue:
            return "Queue is empty"
        
        priority, index, item = heapq.heappop(self._queue)
        return f"Processing: {item} (Priority: {priority})"

    def is_empty(self):
        return len(self._queue) == 0

# --- Example Usage ---
pq = PriorityQueue()

pq.push("Fix critical server bug", 1)   # High priority
pq.push("Check emails", 3)              # Low priority
pq.push("Write documentation", 2)       # Medium priority
pq.push("Reply to Slack message", 2)    # Medium priority (added after docs)

print("\n--- Processing Tasks ---")
while not pq.is_empty():
    print(pq.pop())