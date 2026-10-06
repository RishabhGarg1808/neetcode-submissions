class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k % n
        k_arr = nums[n-k:]

        #shift to right from the n-k postion using two pointers

        i,j = n-k-1,n-1

        while i >=0:
            nums[j] = nums[i]
            j -=1
            i -=1
        
        #now we add the reamin array to k places
        for i, num in enumerate(k_arr):
            nums[i] = num



        