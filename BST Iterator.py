# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []  # Initialize the stack inside the constructor
        self.pushAll(root)

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left  # Move to the left child
    
    def next(self) -> int:
        node = self.stack.pop()  # Get the next smallest element
        self.pushAll(node.right)  # Process the right subtree
        return node.val  # Return the value of the node

    def hasNext(self) -> bool:
        return len(self.stack) > 0  # Return True if there are elements left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
