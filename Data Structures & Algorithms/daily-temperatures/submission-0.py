class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # stores indices
        
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append(i)
            
        return res
