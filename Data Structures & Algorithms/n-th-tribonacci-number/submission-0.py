class Solution:
    def tribonacci(self, n: int) -> int:
        
        seen = [0] * (n + 1)
        def trib(m):
            if m == 0:
                return 0

            if m <=2:
                return 1
            
            if seen[m]:
                return seen[m]

            seen[m] = trib(m-1) + trib(m-2) + trib(m-3)

            return seen[m]

        return trib(n)
        