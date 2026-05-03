from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = res = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
