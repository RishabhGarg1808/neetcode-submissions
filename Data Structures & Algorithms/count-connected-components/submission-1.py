class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [ [] for x in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node):
            for neigh in adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        
        count = 0

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                count +=1
        
        return count
