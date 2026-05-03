class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        zipped_positions_speed = [(x1, x2) for x1, x2 in zip(position, speed)]
        zipped_positions_speed.sort(reverse=True)
        stack = []
        for car in zipped_positions_speed:
            current_time = (target - car[0]) / float(car[-1])
            if not stack or current_time > stack[-1]:
                stack.append(current_time)
        return len(stack)
