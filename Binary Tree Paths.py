# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 
class Solution:
    def DFS(self,root, allPaths, path):
        if not root:
            return
        path.append(str(root.val))

        if not root.left and not root.right:
            allPaths.append('->'.join(path))
        left = self.DFS(root.left, allPaths, path)
        right = self.DFS(root.right, allPaths, path)
        path.pop()
        return 
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        allPaths = []
        path = []
        self.DFS(root,allPaths, path)
        return allPaths

        
        
