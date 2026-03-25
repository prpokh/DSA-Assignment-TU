class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, key):
        temp = self.head

        # Search for the node to delete
        while temp and temp.data != key:
            temp = temp.next

        if temp is None: # Key not found
            return

        # If the node to be deleted is the head node
        if temp == self.head:
            self.head = temp.next

        # Change next only if node to be deleted is NOT the last node
        if temp.next is not None:
            temp.next.prev = temp.prev

        # Change prev only if node to be deleted is NOT the first node
        if temp.prev is not None:
            temp.prev.next = temp.next
        
        temp = None # Free memory

    def display_forward(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print("Forward:  " + " <-> ".join(elements) + " -> None")

    def display_backward(self):
        temp = self.head
        if not temp: return
        
        # Move to the end of the list
        while temp.next:
            temp = temp.next
        
        # Traverse backward using 'prev'
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.prev
        print("Backward: " + " <-> ".join(elements) + " -> None")

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_beginning(5)
    dll.insert_at_beginning(1)

    dll.display_forward()  # Output: Forward:  1 <-> 5 <-> 10 <-> 20 -> None
    dll.display_backward() # Output: Backward: 20 <-> 10 <-> 5 <-> 1 -> None

    print(dll.delete_node(10)) # Deletes node with value 10
    dll.display_forward()  # Output: Forward:  1 <-> 5 <-> 20 -> None