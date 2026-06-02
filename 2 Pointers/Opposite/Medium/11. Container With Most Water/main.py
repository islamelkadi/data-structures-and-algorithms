class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = current_area = maximum_area = 0
        right = len(height) - 1

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maximum_area = max(maximum_area, current_area)
        return maximum_area