class Queue: #circular
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None  # Optional: clear reference
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]
    
#Example use

if __name__ == "__main__":
    q = Queue(5)
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    
    print("Front item:", q.peek())  # 10
    
    print("Dequeue:", q.dequeue())   # 10
    print("Dequeue:", q.dequeue())   # 20
    
    print("Front item after dequeue:", q.peek())  # 30
    
    q.enqueue(60)  # This will work as it's circular
    print("Front item after enqueueing 60:", q.peek())  # 30