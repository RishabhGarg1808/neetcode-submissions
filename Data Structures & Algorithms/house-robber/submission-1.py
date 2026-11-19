class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = [-1] * len(nums)

        def rec(n):
            if n >= len(nums):
                return 0
            if seen[n] == -1:
                seen[n] = max(rec(n+1),nums[n] + rec(n+2 ))
                
            return seen[n]
        
        return rec(0)