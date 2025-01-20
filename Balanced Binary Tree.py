# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
class Solution:
    def checkHeightAndBalance(self, root):
        if not root:
            return 0  # Base case: height of an empty tree is 0

        # Recursively get the height of the left and right subtrees
        leftHeight = self.checkHeightAndBalance(root.left)
        if leftHeight == -1:  # Left subtree is not balanced
            return -1

        rightHeight = self.checkHeightAndBalance(root.right)
        if rightHeight == -1:  # Right subtree is not balanced
            return -1

        # Check if the current node is balanced
        if abs(leftHeight - rightHeight) > 1:
            return -1  # Not balanced

        # Return the height of the current subtree
        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root):
        return self.checkHeightAndBalance(root) != -1


#Time Complexity
# O(n): Each node is visited once, and the height is calculated in the same traversal.
# Space Complexity
# O(h): The function uses recursion, and the space required is proportional to the height of the tree (h), 
    #where h is the height of the binary tree. In the worst case, this is O(n) for a skewed tree and O(log n) for a balanced tree.
