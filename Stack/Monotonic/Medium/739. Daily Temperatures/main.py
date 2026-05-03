class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temperature_tracker = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                _, index = stack.pop()
                temperature_tracker[index] = i - index
            stack.append((temperatures[i], i))
        return temperature_tracker
