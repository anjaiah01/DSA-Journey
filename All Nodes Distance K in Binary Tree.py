from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def parentTrack(self, root: TreeNode) -> dict:
        """
        Function to map child nodes to their parents using BFS.
        """
        parent = {}  # Dictionary to store parent references
        queue = deque([root])  # Initialize queue for BFS
        
        while queue:
            curr = queue.popleft()
            
            # Map left child to current node
            if curr.left:
                parent[curr.left] = curr
                queue.append(curr.left)
            
            # Map right child to current node
            if curr.right:
                parent[curr.right] = curr
                queue.append(curr.right)

        return parent  # Return parent mapping

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Function to find all nodes at distance K from the target node.
        """
        if not root:
            return []
        
        # Step 1: Build Parent Mapping
        parent = self.parentTrack(root)

        # Step 2: Perform BFS from Target Node
        queue = deque([target])  # Start BFS from the target node
        visited = {target: True}  # Mark target as visited
        dist = 0

        while queue:
            size = len(queue)
            if dist == k:
                break  # Stop at required distance
            dist += 1  # Increase distance counter
            
            for _ in range(size):
                curr = queue.popleft()

                # Traverse Left Child
                if curr.left and curr.left not in visited:
                    queue.append(curr.left)
                    visited[curr.left] = True

                # Traverse Right Child
                if curr.right and curr.right not in visited:
                    queue.append(curr.right)
                    visited[curr.right] = True

                # Traverse Parent
                if curr in parent and parent[curr] not in visited:
                    queue.append(parent[curr])
                    visited[parent[curr]] = True
        
        # Step 3: Collect Result
        return [node.val for node in queue]  # Extract values of remaining nodes in queue






# Given the root of a binary tree, the value of a target node target, and an integer k, 
# return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

 
