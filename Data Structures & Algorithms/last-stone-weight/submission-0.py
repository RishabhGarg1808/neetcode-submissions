class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while True:
            if len(stones) <= 1:
                break
            
            x =  heapq.heappop_max(stones)
            y =  heapq.heappop_max(stones)

            if x == y:
                continue
            else:
                heapq.heappush_max(stones, x-y)


        return stones[0] if stones else 0 
