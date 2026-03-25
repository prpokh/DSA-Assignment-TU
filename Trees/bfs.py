from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_search(root, target):
    if root is None:
        return None

    # Initialize queue with the root node
    queue = deque([root])

    while queue:
        # Remove the first node in the queue
        current_node = queue.popleft()

        # Check if this is the value we want
        if current_node.value == target:
            return current_node

        # Add children to the queue for the next level's exploration
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return None # Value not found

# Example Usage:
#      10
#     /  \
#    5    15
#   / \
#  2   7

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

result = bfs_search(root, 7)
print(f"Found node with value: {result.value}" if result else "Value not found")