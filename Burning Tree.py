from collections import deque

class Solution:
    def parentTrack(self, root):
        """Creates a mapping of each node to its parent and finds the target node."""
        parent = {}
        targetNode = None
        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if curr.data == self.targetValue:
                targetNode = curr  # Store the reference to the target node
            
            if curr.left:
                parent[curr.left] = curr  # Map child to parent
                queue.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                queue.append(curr.right)

        return parent, targetNode

    def minTime(self, root, target):
        """Finds the minimum time required to burn the tree starting from target."""
        self.targetValue = target  # Store target value
        parent, targetNode = self.parentTrack(root)  # Get parent mapping and target node
        
        if not targetNode: 
            return 0  # If target not found, return 0

        visited = set()
        queue = deque([targetNode])
        visited.add(targetNode)

        time = -1  # Start with -1 because the first second starts from target itself
        
        while queue:
            size = len(queue)
            time += 1  # Increase time for each level of burning
            
            for _ in range(size):
                curr = queue.popleft()

                # Spread fire to left child
                if curr.left and curr.left not in visited:
                    queue.append(curr.left)
                    visited.add(curr.left)

                # Spread fire to right child
                if curr.right and curr.right not in visited:
                    queue.append(curr.right)
                    visited.add(curr.right)

                # Spread fire to parent
                if curr in parent and parent[curr] not in visited:
                    queue.append(parent[curr])
                    visited.add(parent[curr])

        return time  # Total time taken to burn the entire tree



# Given a binary tree and a node data called target. 
# Find the minimum time required to burn the complete binary tree if the target is set on fire. 
# It is known that in 1 second all nodes connected to a given node get burned. 
# That is its left child, right child, and parent.
# Note: The tree contains unique values.
