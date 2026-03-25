# STACK USING SINGLY LINKED LIST

from .singly_ll import SinglyLinkedList

class Stack:
    def __init__(self):
        # Internal storage using your Singly Linked List
        self._storage = SinglyLinkedList()
        self.size = 0

    def push(self, data):
        # Push is O(1) if we insert at the beginning (head)
        self._storage.insert_at_beginning(data)
        self.size += 1
        print(f"Pushed {data} to stack.")

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        
        # Get data from current head
        popped_node_data = self._storage.head.data
        # Move head pointer to the next node (effectively deleting the top)
        self._storage.head = self._storage.head.next
        self.size -= 1
        return popped_node_data

    def peek(self):
        return self._storage.head.data if self._storage.head else "Stack is empty"

    def is_empty(self):
        return self._storage.head is None

    def display_stack(self):
        print("Stack (Top -> Bottom):")
        self._storage.traverse()

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display_stack()
    print(f"Popped: {stack.pop()}")
    print(f"Top element: {stack.peek()}")

print("------------------------------------------------------")

# QUEUE USING DOUBLY LINKED LIST

from .doubly_ll import DoublyLinkedList

class Queue:
    def __init__(self):
        # Internal storage using your Doubly Linked List
        self._storage = DoublyLinkedList()
        self.size = 0

    def enqueue(self, data):
        # Add to the end of the list
        self._storage.insert_at_end(data)
        self.size += 1
        print(f"Enqueued {data} to queue.")

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        
        # In FIFO, we remove from the front (head)
        dequeued_data = self._storage.head.data
        # Use your existing DLL delete method
        self._storage.delete_node(dequeued_data)
        self.size -= 1
        return dequeued_data

    def is_empty(self):
        return self._storage.head is None

    def display_queue(self):
        print("Queue (Front -> Rear):")
        self._storage.display_forward()

# example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display_queue()
    print(f"Dequeued: {queue.dequeue()}")
    queue.display_queue()