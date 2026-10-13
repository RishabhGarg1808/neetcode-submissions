class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for rows in matrix :
            if rows[0] > target and rows[-1] > target:
                continue
            l,r = 0,len(rows)-1

            while l <= r:
                mid = (l+r) //2

                if rows[mid] == target:
                    return True
                elif rows[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1


        return False 
            