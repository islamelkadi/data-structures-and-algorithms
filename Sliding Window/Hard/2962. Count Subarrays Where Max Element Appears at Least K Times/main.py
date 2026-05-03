from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        left = max_count = res = 0
        for right in range(len(nums)):
            if nums[right] == max_val:
                max_count += 1
            while max_count >= k:
                if nums[left] == max_val:
                    max_count -= 1
                left += 1
            res += left
        return res
