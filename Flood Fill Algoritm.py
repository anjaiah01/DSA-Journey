from typing import List

class Solution:
    def DFS(self, image, sr, sc, initialColor, color):
        # Change the color of the current pixel
        image[sr][sc] = color
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        
        for dr, dc in directions:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == initialColor:
                self.DFS(image, nr, nc, initialColor, color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initialColor = image[sr][sc]
        if initialColor == color:  # If already filled, return original image
            return image
        
        self.DFS(image, sr, sc, initialColor, color)
        return image
