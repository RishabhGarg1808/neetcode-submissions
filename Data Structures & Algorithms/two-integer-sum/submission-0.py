class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        intMap = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in intMap:
                return [intMap[complement],i]
            intMap[n] = i
        
        return []