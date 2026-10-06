class Solution:
    def water(self,x: int,y:int) -> int:
        return x * y

    def maxArea(self, heights: List[int]) -> int:
        area = -1
        n = len(heights)
        i,j = 0,n-1

        while i < j:
            l_area = self.water(min(heights[i],heights[j]),j-i)

            area = max(area,l_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1 
        

        return area