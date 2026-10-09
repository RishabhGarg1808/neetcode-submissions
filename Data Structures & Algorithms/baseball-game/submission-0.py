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
                        stack.remove(stack[-1])
                    case 'D':
                        stack.append(stack[-1] * 2)
        sum = 0
        for o in stack:
            sum += o
        
        return sum


                        


