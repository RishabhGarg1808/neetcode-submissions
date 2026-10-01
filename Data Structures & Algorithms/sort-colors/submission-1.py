class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_r,count_w, count_b = 0,0,0

        for x in nums:
            if x == 0:
                count_r += 1
            elif x == 1:
                count_w += 1
            else :
                count_b += 1

        i = 0 
        for x in range(count_r):
            nums[i] = 0
            i += 1
        for x in range(count_w):
            nums[i] = 1
            i += 1
        for x in range(count_b):
            nums[i] = 2
            i += 1
        
