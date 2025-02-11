# Correct and Optimal Approach:
# A more optimal way to check if a tree is a BST is to use a range-based approach where:

# Each node has a valid range [min_val, max_val] that it must satisfy.
# The left child must be within [min_val, root.data - 1].
# The right child must be within [root.data + 1, max_val].

class Solution:
    def isBST(self, root):
        def validate(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.data < max_val):
                return False
            return validate(node.left, min_val, node.data) and validate(node.right, node.data, max_val)

        return validate(root, float('-inf'), float('inf'))
