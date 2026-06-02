from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        # Initialize pointers and constraint tracker
        left = ans = 0
        curr = 1 # To avoid zeroing out all the time

        # Iterate over list
        for right in range(len(nums)):
            curr *= nums[right]
            # Check if constraint broken
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
