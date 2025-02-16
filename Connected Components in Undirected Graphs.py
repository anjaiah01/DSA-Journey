from collections import deque

class Solution:
    # Function to return connected components of the graph
    def BFS(self, adj, visited, start):
        component = []
        queue = deque([start])
        visited[start] = True
        component.append(start)
        
        while queue:
            i = queue.popleft()
            for v in adj[i]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
                    component.append(v)
        
        return component

    def connectedcomponents(self, v, edges):
        visited = [False for _ in range(v)]
        conComponents = []
        
        # Step 1: Build adjacency list
        adj = {i: [] for i in range(v)}
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)
        
        # Step 2: BFS for each connected component
        for i in range(v):
            if not visited[i]:
                conComponents.append(self.BFS(adj, visited, i))
        
        return conComponents
