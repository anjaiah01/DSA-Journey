class Solution:
    def __init__(self):
        self.maxiSum = float('-inf')  # Initialize to negative infinity

    def maxGain(self, node):
        if not node:
            return 0  # Base case: no contribution from an empty node

        # Recursively calculate the maximum gain from the left and right subtrees
        leftGain = max(self.maxGain(node.left), 0)  # Ignore negative paths
        rightGain = max(self.maxGain(node.right), 0)

        # Calculate the path sum that passes through the current node
        currentPathSum = node.val + leftGain + rightGain

        # Update the global maximum path sum
        self.maxiSum = max(self.maxiSum, currentPathSum)

        # Return the maximum gain of a single path ending at the current node
        return node.val + max(leftGain, rightGain)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxGain(root)  # Start the recursion
        return self.maxiSum  # Return the global maximum path sum




# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.
