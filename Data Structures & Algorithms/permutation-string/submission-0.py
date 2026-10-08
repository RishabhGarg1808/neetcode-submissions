class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)

        n = len(s2)

        count1 = [0] *26
        count2 = [0] *26

        if m > n:
            return False

        for c in s1:
            count1[ord(c) -ord('a')] +=1
        for i in range(m):
            count2[ord(s2[i]) -ord('a')] += 1
        
        if count1==count2:
            return True

        for i in range(m,n):
            count2[ord(s2[i]) - ord('a')] +=1

            count2[ord(s2[i-m]) - ord('a')] -=1

            if count1 == count2:
                return True

        return False