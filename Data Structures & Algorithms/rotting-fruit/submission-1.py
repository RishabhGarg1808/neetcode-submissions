class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows ,cols =  len(grid), len(grid[0])
        freshCount = 0
        
        visited = set()
        q =  deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshCount += 1
                
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append([r,c])
        def addRows(r,c):
            nonlocal freshCount
            if r < 0 or c <0 or r >= rows or c >= cols \
            or grid[r][c] == 0 or (r,c) in visited:
                return
            if grid[r][c] == 1:
                freshCount -= 1
                grid[r][c] = 2
            visited.add((r,c))
            q.append([r,c])

        time = 0
        if freshCount == 0:
            return 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                addRows(r+1,c)
                addRows(r-1,c)
                addRows(r,c+1)
                addRows(r,c-1)
            time += 1

            if freshCount <= 0:
                return time
        
        return -1

            

        

