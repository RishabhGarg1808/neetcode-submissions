class Solution:
    def climbStairs(self, n: int) -> int:
        seen = [0] *n
        def rec(i):
            if i == n :
                return 1
            if i > n:
                return 0
            
            if seen[i]:
                return seen[i] 
            seen[i] = rec(i + 1) + rec(i + 2)
            return seen[i]
        
        return rec(0)