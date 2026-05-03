from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = curr = 0
        for num in nums:
            curr += num
            min_sum = min(min_sum, curr)
        return max(1, 1 - min_sum)
