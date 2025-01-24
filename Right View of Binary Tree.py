from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        rightView = []
        queue = deque([root])  # BFS queue
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                # Add the last node of each level
                if i == level_size - 1:
                    rightView.append(node.val)
                
                # Add left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return rightView
