class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_map = {}

        for x in nums:
            k_map[x] = k_map.get(x,0) + 1 
        
        bucket = [[] for _ in range(len(nums) +1 )]
        
        for num,count in k_map.items():
            bucket[count].append(num)
        
        result = []

        for count in range(len(bucket) -1,0, -1):
            for num in bucket[count]:
                result.append(num)

                if len(result) == k:
                    return result
        
        return result

