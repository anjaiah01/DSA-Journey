from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []

        # Dictionary to store the bottom-most node at each horizontal distance
        hd_map = {}
        # Queue for BFS, stores tuples of (node, horizontal distance)
        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            # Update the node for the current horizontal distance
            hd_map[hd] = node.data

            # Add left and right children to the queue with updated HDs
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        # Extract the bottom view in sorted order of horizontal distances
        bottom_view = []
        for hd in sorted(hd_map.keys()):
            bottom_view.append(hd_map[hd])

        return bottom_view
