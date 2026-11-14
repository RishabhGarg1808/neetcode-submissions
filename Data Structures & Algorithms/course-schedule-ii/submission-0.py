class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegre = [0] *numCourses
        adj = [[] for x in range(numCourses)]

        q = deque()
        res = []

        for dst,src in prerequisites:
            indegre[dst] += 1
            adj[src].append(dst)
        
        for i, n in enumerate(indegre):
            if n == 0:
                q.append(i)

        processed = 0
        while q:
            node = q.popleft()
            processed += 1
            res.append(node)

            for neigh in adj[node]:
                indegre[neigh] -= 1
                if indegre[neigh] ==  0:
                    q.append(neigh)
        
        if processed != numCourses:
            return []
        
        return res


