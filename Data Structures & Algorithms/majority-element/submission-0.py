class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntMap ={}
        
        for x in nums:
            if x not in cntMap:
                cntMap[x] = 1
            else:
                cntMap[x] = cntMap[x] + 1
        

        return max(cntMap, key=cntMap.get)