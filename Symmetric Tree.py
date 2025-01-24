# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class Solution:
    # Helper function to check if two trees are mirror images of each other
    def isSymmetricUtility(self, root1, root2):
        # If either tree is None, return True only if both are None
        if root1 == None or root2 == None:
            return root1 == root2
        
        # Check if:
        # 1. Current node values are equal
        # 2. Left subtree of root1 matches right subtree of root2
        # 3. Right subtree of root1 matches left subtree of root2
        return (root1.val == root2.val) and \
               (self.isSymmetricUtility(root1.left, root2.right)) and \
               self.isSymmetricUtility(root1.right, root2.left)
    
    # Main function to check if the tree is symmetric
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # An empty tree is symmetric
        if not root:
            return True
        
        # A tree with no children is symmetric
        if root.left == None and root.right == None:
            return True
        
        # Use the helper function to check if left and right subtrees are mirror images
        return self.isSymmetricUtility(root.left, root.right)
