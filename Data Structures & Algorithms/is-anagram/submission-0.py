class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charmap_s = dict()
        charmap_t = dict()

        for c in s:
            charmap_s[c] = charmap_s.get(c,0) + 1
        
        for c in t:
            charmap_t[c] = charmap_t.get(c,0) + 1

        return charmap_s == charmap_t
        
        