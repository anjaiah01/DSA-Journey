from collections import deque
from typing import List  # ✅ Import List for function annotation

class Solution:
    def BFS(self, grid: List[List[str]], visited: List[List[bool]], i: int, j: int):
        queue = deque([(i, j)])  # ✅ Fix queue initialization
        visited[i][j] = True  # ✅ Mark the cell as visited
        
        # Directions for moving in 4 possible ways (Right, Down, Left, Up)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # ✅ Check boundaries and if it's unvisited land
                if (0 <= new_row < len(grid) and
                    0 <= new_col < len(grid[0]) and
                    not visited[new_row][new_col] and
                    grid[new_row][new_col] == '1'):
                    
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = True  # ✅ Mark as visited

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0  # Edge case: Empty grid
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        islands = 0  # ✅ Initialize island count

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:  # ✅ Only process unvisited land cells
                    islands += 1  # ✅ Found a new island
                    self.BFS(grid, visited, i, j)  # ✅ Run BFS to mark all connected land

        return islands

# ✅ Example Usage:
sol = Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(sol.numIslands(grid))  # ✅ Expected Output: 3
