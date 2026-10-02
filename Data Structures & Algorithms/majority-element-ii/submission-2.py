class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0) +1
        n = len(nums)

        return [ num for num ,count in freq_map.items() if count > n/3]