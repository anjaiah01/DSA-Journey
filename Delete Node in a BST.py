
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None  # If tree is empty or key not found

        # Step 1: Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)  # Go left
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)  # Go right
        else:
            # Step 2: Node to delete found

            # Case 1: No child (Leaf node)
            if not root.left and not root.right:
                return None
            
            # Case 2: One child (left or right)
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: Two children
            # Find inorder successor (smallest node in right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val  # Replace value
            root.right = self.deleteNode(root.right, successor.val)  # Delete the successor

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node














# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105
 

# Follow up: Could you solve it with time complexity O(height of tree)?
