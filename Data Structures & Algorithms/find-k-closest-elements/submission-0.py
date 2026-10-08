class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        res = {}
        n=len(arr)

        if k == n:
            return arr
        
        min_diff = float('inf')
        best_start = 0

        for i in range(n-k+1):
            diff =0 
            for j in range(i,i+k):
                diff += abs(arr[j] - x)
            
            if diff < min_diff:
                min_diff =diff
                best_start =i 
            
        
        return arr[best_start:best_start+k]


