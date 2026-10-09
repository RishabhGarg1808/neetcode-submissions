class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        groups = {
            '}' : '{',
            ')' : '(',
            ']' : '[' ,
            
        }

        for c in s:
            if c in groups:
                if stack and stack[-1] == groups[c] :
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        

        return (True if len(stack) == 0  else False)