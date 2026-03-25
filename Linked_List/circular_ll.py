class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        # Traverse to the last node
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to Head)")

    def delete(self, key):
        if self.head is None:
            return

        curr = self.head
        prev = None

        # Case 1: Deleting the Head
        if curr.data == key:
            # If there's only one node
            if curr.next == self.head:
                self.head = None
                return
            
            # Find the last node to update its pointer
            last = self.head
            while last.next != self.head:
                last = last.next
            
            self.head = self.head.next
            last.next = self.head
            return

        # Case 2: Deleting middle or last node
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == key:
                prev.next = curr.next
                return
            
# example usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert(10)
    cll.insert(20)
    cll.insert(30)
    cll.insert(40)

    print("Circular Linked List after insertion:")
    cll.traverse()

    cll.delete(20)
    print("\nCircular Linked List after deleting 20:")
    cll.traverse()

    cll.delete(10)
    print("\nCircular Linked List after deleting 10 (head):")
    cll.traverse()