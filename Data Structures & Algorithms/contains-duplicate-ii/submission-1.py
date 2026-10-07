class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_map ={}

        n= len(nums)

        for i,n in enumerate(nums):
            if n in seen_map:
                for x in seen_map[n]:
                    if abs(x - i) <=k:
                        return True
                seen_map[n].append(i)
            else:
                seen_map[n] = [i]
        
        return False