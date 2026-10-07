class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       window = set()   
       n = len(nums)
       L =0 

       for R in range(n):
        if R-L > k :
            window.remove(nums[L])
            L+=1
        if nums[R] in window:
            return True
        window.add(nums[R])
    
       return False