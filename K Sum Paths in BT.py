class Solution:
    def countPaths(self, root, targetSum, prefix_sum_map, current_sum):
        if not root:
            return 0
        
        # Update the current prefix sum
        current_sum += root.data
        
        # Check if a valid path sum exists
        num_paths = prefix_sum_map.get(current_sum - targetSum, 0)
        
        # Update prefix sum map (Include current sum)
        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1
        
        # Recur for left and right subtrees
        num_paths += self.countPaths(root.left, targetSum, prefix_sum_map, current_sum)
        num_paths += self.countPaths(root.right, targetSum, prefix_sum_map, current_sum)
        
        # Backtrack (Remove current node's prefix sum from the map)
        prefix_sum_map[current_sum] -= 1
        if prefix_sum_map[current_sum] == 0:
            del prefix_sum_map[current_sum]
        
        return num_paths
    
    def sumK(self, root, k):
        prefix_sum_map = {0: 1}  # Base case: A sum of 0 exists initially
        return self.countPaths(root, k, prefix_sum_map, 0)




# Given a binary tree and an integer k, determine the number of downward-only paths 
# where the sum of the node values in the path equals k. A path can start and end
# at any node within the tree but must always move downward (from parent to child).

# Examples:

# Input: k = 7   

# Output: 3
# Explanation: The following paths sum to k 
 
# Input: k = 3

# Output: 2
# Explanation:
# Path 1 : 1 -> 2 (Sum = 3)
# Path 2 : 3 (Sum = 3)


# Constraints:

# 1 ≤ number of nodes ≤ 104
# -100 ≤ node value ≤ 100
# -109 ≤ k ≤ 109
