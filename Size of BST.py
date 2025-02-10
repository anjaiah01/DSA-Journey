class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getSize(self, root: TreeNode) -> int:
        if not root:
            return 0  # Base case: Empty tree has size 0
        
        # Recursively compute the size of left and right subtrees
        left_size = self.getSize(root.left)
        right_size = self.getSize(root.right)
        
        return 1 + left_size + right_size  # Current node + left subtree + right subtree
