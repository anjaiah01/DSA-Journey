from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Initialize queue with (node, index), where index represents position in the tree
        queue = deque([(root, 0)])
        maxWidth = 0  # Store the maximum width found
        
        while queue:
            size = len(queue)
            _, first_index = queue[0]  # Get the first node's index in the level
            _, last_index = queue[-1]  # Get the last node's index in the level
            maxWidth = max(maxWidth, last_index - first_index + 1)  # Update max width
            
            for _ in range(size):
                node, index = queue.popleft()  # Dequeue the current node
                
                # Append left child with the proper index
                if node.left:
                    queue.append((node.left, 2 * index))
                
                # Append right child with the proper index
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return maxWidth










# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.
