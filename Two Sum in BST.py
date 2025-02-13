# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Brute-Force Approach 
#Find the Inorder of the BST, then apply the two pointers technique on the inorder list
#Time complexity for brute-force TC - O(N)+O(logN)
#Space complexity for brute-force SC - O(N)
class Solution:
    def inorder(self, root, res):
        if not root:
            return None
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
        return 

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []
        self.inorder(root,res)
        left , right = 0, len(res)-1
        while left < right:
            s = res[left]+res[right]
            if s == k:
                return True
            elif s>k:
                right-=1
            else:
                left+=1
        return False






# Given the root of a binary search tree and an integer k, 
# return true if there exist two elements in the BST 
# such that their sum is equal to k, or false otherwise.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 
# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105
