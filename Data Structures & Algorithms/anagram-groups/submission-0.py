class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anMap = {}

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] = arr[ord(c) - ord('a')] +1

            key = tuple(arr)
            if key not in anMap:
                anMap[key] = []
            anMap[key].append(s)


        return list(anMap.values())   
        