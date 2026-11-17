class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        seen = [0] * len(cost)
        def rec(i):
            if i >= len(cost):
                return 0
            if seen[i]:
                return seen[i]

            seen[i] = cost[i] + min(rec(i+1), rec(i+2))
            return seen[i]
        

        return min(rec(0),rec(1))
            
