class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_map = {}

        for x in nums:
            if x not in k_map:
                k_map[x] = 1
            else:
                k_map[x] += 1
        
        sorted_map = sorted(k_map,key=k_map.get,reverse= True)

        return sorted_map[:k]

