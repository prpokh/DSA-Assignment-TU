class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

# --- Example Usage ---

# 1. Create the root
root = TreeNode("Electronics")

# 2. Create categories (Children of root)
laptop = TreeNode("Laptops")
phone = TreeNode("Cell Phones")

root.add_child(laptop)
root.add_child(phone)

# 3. Create specific items (Children of categories)
laptop.add_child(TreeNode("MacBook Pro"))
laptop.add_child(TreeNode("Surface Pro"))
phone.add_child(TreeNode("iPhone 15"))

# 4. Retrieve/Display the structure
root.print_tree()