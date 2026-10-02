class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the '#'
            j = i

            while s[j] != '#':
                j += 1

            # Convert length to integer
            length = int(s[i:j])

            # Read exactly `length` characters
            start = j + 1
            end = start + length

            res.append(s[start:end])

            # Move to next encoded string
            i = end

        return res