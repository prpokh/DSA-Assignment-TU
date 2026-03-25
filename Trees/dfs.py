class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_search(node, target):
    # Base case: we hit a leaf's child or the tree is empty
    if node is None:
        return None

    # Check if this node is the one we want
    if node.value == target:
        return node

    # Search the left subtree
    found_left = dfs_search(node.left, target)
    if found_left:
        return found_left

    # If not in left, search the right subtree
    return dfs_search(node.right, target)

# Example Tree Setup
#      A(10)
#     /    \
#   B(5)   C(15)
#   /
# D(2)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)

result = dfs_search(root, 15)
print(f"Node found: {result.value}" if result else "Not found")