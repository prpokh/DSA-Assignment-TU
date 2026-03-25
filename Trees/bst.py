class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)
        # If key == current.key, we do nothing (no duplicates)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        # Base Case: Not found or found the node
        if current is None or current.key == key:
            return current

        # Value is greater than node's key
        if key > current.key:
            return self._search_recursive(current.right, key)

        # Value is smaller than node's key
        return self._search_recursive(current.left, key)

# --- Example Usage ---
bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80]

for el in elements:
    bst.insert(el)

# Search for a value
target = 60
result = bst.search(target)

if result:
    print(f"Found {target} in the BST!")
else:
    print(f"{target} not found.")