class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r= 0,0
        n = len(s)
        count = [0] *26
        max_len = 0

        for r in range(n):
            count[ord(s[r]) - ord('A')] +=1
            most_freq = max(count)

            if (r-l+1) - most_freq  <=k:
                max_len = max(max_len,(r-l+1))
            else:
                count[ord(s[l])-ord('A')] -=1
                l +=1
        

        return max_len
