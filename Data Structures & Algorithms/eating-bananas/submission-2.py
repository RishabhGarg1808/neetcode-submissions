class Solution:
    def can_consume(self, piles : List[int], h, k) -> bool:
        for x in piles:
            h -= math.ceil(x/k)
            if h < 0:
                return False

        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        i , j = 1, max(piles)
        res = j
        while i <=j:
            mid = (i+j) //2
            if self.can_consume(piles,h,mid):
                res = min(res,mid)
                j = mid - 1 
            else:
                i = mid +1


        return res