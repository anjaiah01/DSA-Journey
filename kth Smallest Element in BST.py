# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, counter, kthSmall, k):
        if not root or counter[0] >= k:
            return
        
        self.inorder(root.left, counter, kthSmall, k)  # Left subtree
        
        counter[0] += 1
        if counter[0] == k:
            kthSmall[0] = root.val
            return
        
        self.inorder(root.right, counter, kthSmall, k)  # Right subtree
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]  # Mutable list to store count
        kthSmall = [0]  # Mutable list to store kth smallest value
        self.inorder(root, counter, kthSmall, k)
        return kthSmall[0]
