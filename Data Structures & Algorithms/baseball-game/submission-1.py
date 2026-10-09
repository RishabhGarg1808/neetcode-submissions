class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o not in ['+','C','D']:
                stack.append(int(o))
            else:
                match o :
                    case '+':
                        stack.append(stack[-1]+stack[-2])
                    case 'C':
                        stack.pop()
                    case 'D':
                        stack.append(stack[-1] * 2)
        return sum(stack)


                        


