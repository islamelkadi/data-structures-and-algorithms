from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        pos = n - 1  # Position to fill in the result array
        while pos >= 0:
            if abs(nums[right]) >= abs(nums[left]):
                result[pos] = nums[right] ** 2
                right -= 1
            else:
                result[pos] = nums[left] ** 2
                left += 1
            pos -= 1
        return result
