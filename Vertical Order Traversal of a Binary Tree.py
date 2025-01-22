from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Map to store nodes by vertical and level
        map = defaultdict(lambda: defaultdict(list))  # vertical: {level: (nodes)}
        queue = deque([(root, (0, 0))])  # Queue for BFS traversal (node, (vertical, level))
        verticalView = [] 

        # Perform BFS traversal
        while queue:
            node, (vertical, level) = queue.popleft()
            map[vertical][level].append(node.val)

            if node.left:
                queue.append((node.left, (vertical - 1, level + 1)))
            if node.right:
                queue.append((node.right, (vertical + 1, level + 1)))

        # Process the map in sorted order of vertical and level
        for vertical in sorted(map.keys()):  # Sort by vertical
            verticalLine = []
            for level in sorted(map[vertical].keys()):  # Sort by level
                verticalLine.extend(sorted(map[vertical][level]))  # Sort node values
            verticalView.append(verticalLine)

        return verticalView



# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. 
# The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings 
#   for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes
# in the same row and same column. In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.
