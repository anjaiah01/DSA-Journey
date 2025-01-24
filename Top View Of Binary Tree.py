from collections import deque

class Solution:
    # Function to return a list of nodes visible from the top view 
    # from left to right in Binary Tree.
    def topView(self, root):
        if not root:
            return []

        # Dictionary to store the first node at each vertical level
        vertical_map = {}
        # Queue for BFS traversal, stores tuples of (node, vertical)
        queue = deque([(root, 0)])

        while queue:
            node, vertical = queue.popleft()

            # If this vertical is not yet visited, add it to the map
            if vertical not in vertical_map:
                vertical_map[vertical] = node.data

            # Add left and right children to the queue
            if node.left:
                queue.append((node.left, vertical - 1))
            if node.right:
                queue.append((node.right, vertical + 1))

        # Extract the nodes in sorted order of vertical levels
        top_view = []
        for vertical in sorted(vertical_map.keys()):
            top_view.append(vertical_map[vertical])

        return top_view




# You are given a binary tree, and your task is to return its top view. 
# The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

# Note: 

# Return the nodes from the leftmost node to the rightmost node.
# If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree, consider the leftmost node only. 
