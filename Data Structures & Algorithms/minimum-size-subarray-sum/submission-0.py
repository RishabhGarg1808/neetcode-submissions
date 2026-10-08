class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len = float('inf')
        n = len(nums)

        i,j =0,0

        sum = 0
        for j in range(n):
            sum += nums[j]
            while sum >= target:
                min_len = min(min_len,j-i+1)
                sum -= nums[i]
                i+=1
               


        if min_len== float('inf'):
            return 0
        
        return min_len