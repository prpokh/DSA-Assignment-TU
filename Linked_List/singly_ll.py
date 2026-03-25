class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(nodes) + " -> None")

    def search(self, key):
        temp = self.head
        index = 0
        while temp:
            if temp.data == key:
                return f"Found {key} at index {index}"
            temp = temp.next
            index += 1
        return "Value not found"
    
    def delete_node(self, key):
        temp = self.head

        # Case 1: Head node holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Case 2: Search for the key to be deleted
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Case 3: Key not found
        if temp is None:
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.traverse()  # Output: 5 -> 10 -> 20 -> None
    print(ll.search(10))  # Output: Found 10 at index 1
    print(ll.search(15))  # Output: Value not found
    ll.delete_node(10)
    ll.traverse()  # Output: 5 -> 20 -> None