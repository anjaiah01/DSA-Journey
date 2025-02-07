# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def indexInorder(self, inorder):
        """
        Build a dictionary mapping each value in 'inorder' to its index.
        This helps in quickly finding the root index.
        """
        indexMap = {}
        for index, value in enumerate(inorder):
            indexMap[value] = index
        return indexMap

    def buildBinaryTree(self, inorder, postorder, in_start, in_end, post_start, post_end, indexMap):
        """
        Recursively builds the binary tree from inorder and postorder traversals.

        Parameters:
          - inorder: List[int] of inorder traversal values.
          - postorder: List[int] of postorder traversal values.
          - in_start, in_end: current boundaries in the inorder array.
          - post_start, post_end: current boundaries in the postorder array.
          - indexMap: dictionary mapping a node value to its index in inorder.

        Returns:
          The root node of the constructed subtree.
        """
        # Base case: If there are no elements to construct the subtree.
        if in_start > in_end or post_start > post_end:
            return None
        
        # The last element in the current postorder segment is the root.
        root_val = postorder[post_end]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder traversal.
        root_index = indexMap[root_val]
        # Number of nodes in the left subtree.
        left_count = root_index - in_start
        
        # Recursively build the left subtree:
        # Inorder boundaries: in_start to root_index - 1.
        # Postorder boundaries: post_start to post_start + left_count - 1.
        root.left = self.buildBinaryTree(
            inorder, postorder,
            in_start, root_index - 1,
            post_start, post_start + left_count - 1,
            indexMap
        )
        
        # Recursively build the right subtree:
        # Inorder boundaries: root_index + 1 to in_end.
        # Postorder boundaries: post_start + left_count to post_end - 1.
        root.right = self.buildBinaryTree(
            inorder, postorder,
            root_index + 1, in_end,
            post_start + left_count, post_end - 1,
            indexMap
        )
        
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs the binary tree from inorder and postorder traversal arrays.
        """
        # Create a mapping from node value to its index in inorder traversal.
        indexMap = self.indexInorder(inorder)
        n = len(inorder)
        # Call the recursive helper with initial boundaries.
        return self.buildBinaryTree(inorder, postorder, 0, n - 1, 0, n - 1, indexMap)
