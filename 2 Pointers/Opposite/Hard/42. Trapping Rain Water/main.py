# TWO_POINTERS

# NOTE: YOU NEED TO KEEP IN MIND YOU DO NOT KNOW `DURING RUNTIME` IF THERE ARE
# OBSTACLES. HENCE, YOU NEED TO BRING THE LEFT INWARDS IF THE RIGHT IS BIGGER
# THAN IT SO YOU CAN EXPLORE POTENTIALLY STORING MORE WATER. AND THE SAME APPLIES
# TO THE RIGHT SIDE.

# THE ONLY WAY YOU CAN KNOW UP FRONT WHAT YOUR OBSTACLES ARE IS IF YOU USE A 
# PREFIX SUM APPROACH TO TRACK OBSTACLES FROM THE LEFT, AND SUFFIX SUM APPROACH
# TO TRACK OBSTACLES FROM THE RIGHT.

class Solution:
    def trap(self, height: List[int]) -> int:

        # SLIDING_WINDOW APPROACH
        right = len(height) - 1
        left = max_left = max_right = trapped = 0

        while left < right:
            current_left = height[left]
            current_right = height[right]

            max_left = max(max_left, current_left)
            max_right = max(max_right, current_right)

            if max_left < max_right:
                trapped += max_left - current_left
                left += 1
            else:
                trapped += max_right - current_right
                right -= 1

        return trapped