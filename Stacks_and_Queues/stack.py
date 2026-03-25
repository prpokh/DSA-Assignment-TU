class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        # Pre-allocate the fixed-size array
        self.stack = [None] * capacity
        self.top = -1  # Points to the current top element

    def is_full(self):
        return self.top == self.capacity - 1

    def is_empty(self):
        return self.top == -1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None  # Optional: Clear reference
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]

    def size(self):
        return self.top + 1
    
# Example usage
if __name__ == "__main__":  
    stack = Stack(5)
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    print("Peek:", stack.peek())  # 40
    print("Pop:", stack.pop())    # 40
    print("Size:", stack.size())  # 3
    
    print("Peek after pop:", stack.peek())  # 30