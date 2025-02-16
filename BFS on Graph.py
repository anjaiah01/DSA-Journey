from collections import deque
from typing import List
class Solution:
    def BFS(self, visited, adj, start,bfsGraph):
        queue = deque([start])
        visited[start] = True
        bfsGraph.append(start)
        while queue:
            node = queue.popleft()
            for v in adj[node]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
                    bfsGraph.append(v)
                    
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        bfsGraph = []
        visited = [False] * len(adj)
        
        
        self.BFS(visited, adj, 0, bfsGraph)
        return bfsGraph
