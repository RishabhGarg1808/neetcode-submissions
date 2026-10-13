class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2 :
            return x 
       
        l, r = 1, x//2

        while l <= r:
            mid = (l +r )//2

            if (mid*mid ) == x:
                return mid
            
            if (mid*mid ) > x:
                r =  mid -1
            else:
                l= mid + 1
        
        return r

        
        