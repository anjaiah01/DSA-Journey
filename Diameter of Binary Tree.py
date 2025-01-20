# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

####Optimal Approach
# The O(N2) time complexity of the previous approach can be optimised by eliminating the steps of repeatedly calculating subtree heights. 
# The heights of the left and right subtrees are computed multiple times for each node, which leads to redundant calculations.
# Instead, we can compute these heights in a bottom-up manner. 
# The Postorder method allows us to validate balance conditions efficiently during the traversal.
##Algorithm:

# Step 1: Initialise a variable `diameter` to store the diameter of the tree. Create a function height that takes a node and a reference to the diameter variable as input.

# Step 2: Base Case: If the node is null, return 0 indicating the height of an empty tree.

# Step 3: Recursive Function:

# Recursively calculate the height of the left subtree then height of the right subtree.
# Set the current diameter as the sum of left subtree, right subtree + 1 for the current level.
# Update the diameter with the maximum of the current diameter and the global diameter.

# Step 4: After the traversal if complete, return the maximum diameter found during the traversal as the result.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter=0

    def height(self, root):
       if not root:
        return 0

       lh = self.height(root.left)
       rh = self.height(root.right)
       self.diameter = max(self.diameter, lh+rh)

       return max(lh,rh)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.diameter
