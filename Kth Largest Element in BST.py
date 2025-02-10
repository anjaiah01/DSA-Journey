# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def reverseInorder(self, root, counter, kthLarger, k):
        if not root or counter[0] >= k:
            return
        
        # First, visit right subtree (since it contains larger values)
        self.reverseInorder(root.right, counter, kthLarger, k)
        
        counter[0] += 1
        if counter[0] == k:
            kthLarger[0] = root.data
            return
        
        # Then, visit left subtree
        self.reverseInorder(root.left, counter, kthLarger, k)
        
    def kthLargest(self, root, k):
        counter = [0]  # Mutable counter
        kthLarger = [0]  # Store kth largest value
        self.reverseInorder(root, counter, kthLarger, k)
        return kthLarger[0]
