class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if abs(asteroids[i]) < abs(stack[-1]):
                    break
                if abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    break
                if abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
            else:
                stack.append(asteroids[i])
        return stack
