# Class to represent a Node in the Binary Tree
class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

# Class to represent the Binary Tree
class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    # Function to add a node to the tree
    def add(self, value):
        queue = [self.root]  # Use a queue for level-order insertion
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = TreeNode(value)
                break
            else:
                queue.append(current.left)
            if not current.right:
                current.right = TreeNode(value)
                break
            else:
                queue.append(current.right)

    # Pre-order Traversal (Root -> Left -> Right)
    def preorder_traversal(self, node):
        if not node:
            return []
        return [node.value] + self.preorder_traversal(node.left) + self.preorder_traversal(node.right)

    # In-order Traversal (Left -> Root -> Right)
    def inorder_traversal(self, node):
        if not node:
            return []
        return self.inorder_traversal(node.left) + [node.value] + self.inorder_traversal(node.right)

    # Post-order Traversal (Left -> Right -> Root)
    def postorder_traversal(self, node):
        if not node:
            return []
        return self.postorder_traversal(node.left) + self.postorder_traversal(node.right) + [node.value]

    # Level-order Traversal (Breadth-First Search)
    def level_order_traversal(self):
        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

# Example Usage
if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree(1)  # Root node with value 1
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)

    # Traversals
    print("Pre-order Traversal:", tree.preorder_traversal(tree.root))  # [1, 2, 4, 5, 3, 6, 7]
    print("In-order Traversal:", tree.inorder_traversal(tree.root))    # [4, 2, 5, 1, 6, 3, 7]
    print("Post-order Traversal:", tree.postorder_traversal(tree.root))  # [4, 5, 2, 6, 7, 3, 1]
    print("Level-order Traversal:", tree.level_order_traversal())  # [1, 2, 3, 4, 5, 6, 7]
