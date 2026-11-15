class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for x in range(len(edges) + 1)]
        
        def dfs(node,par):
            if node in visited:
                return True
            
            visited.add(node)

            for neigh in adj[node]:
                if neigh == par:
                    continue
                if dfs(neigh,node):
                    return True
            
            return False
        res = []
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visited = set()
            if dfs(a,-1):
                return[a,b]
        
        return res[-1]
