class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegre = [0] * numCourses
        #calculate indegre
        adj = [[] for i in range(numCourses)]
        for a,b in prerequisites:
            indegre[b] += 1
            adj[a].append(b)
        
        q = deque()    
        #add the 0 indegree nodes to the queue
        for i, n in enumerate(indegre):
            if n == 0:
                q.append(i)
        processedNodes = 0

        while q:
            node = q.popleft()
            processedNodes +=1

            for neigh in adj[node]:
                indegre[neigh] -= 1
                if indegre[neigh] == 0:
                    q.append(neigh)
        
        return processedNodes == numCourses

            

            

