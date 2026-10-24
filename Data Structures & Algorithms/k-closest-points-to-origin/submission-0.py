class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        #calcualte the distance  and insert into the min heap 
        for coord in points:
            d = math.sqrt((coord[0])**2 + (coord[1]**2))
            heap_tup = (d,coord[0],coord[1])
            heapq.heappush(min_heap,heap_tup)
        
        res = []

        while k:
            heap_val = heapq.heappop(min_heap)
            res.append([heap_val[1],heap_val[2]])
            k -= 1 
        
        return res

