class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:
            alive = True

            while stack and stack[-1] > 0 and x < 0:
                if stack[-1] < abs(x):
                    stack.pop()
                elif stack[-1] == abs(x):
                    stack.pop()
                    alive=False
                    break
                else:
                    alive =False
                    break
            if alive:
                stack.append(x)

        return stack
                 