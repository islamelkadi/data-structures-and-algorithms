class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        largest_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            lower_height = min(height[left], height[right])
            length = right - left
            area = lower_height * length
            largest_area = max(largest_area, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return largest_area