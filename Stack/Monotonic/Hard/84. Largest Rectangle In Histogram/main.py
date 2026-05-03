class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        for i, current_height in enumerate(heights):
            while stack and stack[-1][0] > current_height:
                popped_height, index = stack.pop()
                # You are doing a -1 (e.g. i - index - 1)
                # to get the left most boundary of the bar
                # that was just popped.

                # The stack[-1] represents the left boundary
                # which is the bar that hasn't been popped.
                width = i if not stack else i - stack[-1][-1] - 1
                max_area = max(max_area, popped_height * width)
            stack.append((current_height, i))
        
        while stack:
            popped_height, index = stack.pop()
            # Len of heights because your i is now equal to len(heights)
            # meaning you've done a complete first pass on the right side
            width = len(heights) if not stack else len(heights) - stack[-1][-1] - 1
            max_area = max(max_area, popped_height * width)
        return max_area
