class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        
        adj = [[] for x in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        q = deque()

        q.append((0,-1))
        visited.add(0)

        while q:

            node,parent = q.popleft()

            for neigh in adj[node]:
                if neigh == parent:
                    continue
                
                if neigh in visited:
                    return False
                
                visited.add(neigh)
                q.append((neigh,node))
        
        return len(visited) == n
        
