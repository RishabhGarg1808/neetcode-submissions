class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # Extract the encoded substring
                curr = ""
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr

                stack.pop()  # Remove '['

                # Extract the repetition count
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # Repeat the substring and push it back
                stack.append(curr * int(num))

        return "".join(stack)