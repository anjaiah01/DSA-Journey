from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        
        serialized = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                serialized.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialized.append("#")  # Representing null
        
        return ",".join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))  # Convert string to integer
        queue = deque([root])
        i = 1

        while queue and i < len(data):
            node = queue.popleft()
            
            # Process left child
            if data[i] != "#":
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            
            # Process right child
            if i < len(data) and data[i] != "#":
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1

        return root
















# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted across a network connection 
# link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how 
# your serialization/deserialization algorithm should work. You just need to ensure that a binary 
# tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
#You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.




 
