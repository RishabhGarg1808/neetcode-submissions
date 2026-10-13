class Solution:
    def can_ship(self, weights: List[int], days: int, k: int) -> bool:
        cap = k
        l_cap = 0

        for x in weights:
            if l_cap + x > cap:
                l_cap = 0
                days -= 1

            l_cap += x

            if days < 0:
                return False

        return days >= 1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2

            if self.can_ship(weights, days, mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res