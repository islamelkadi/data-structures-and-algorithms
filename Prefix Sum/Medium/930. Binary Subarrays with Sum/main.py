from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        curr_sum = count = 0
        for num in nums:
            curr_sum += num
            count += prefix_count[curr_sum - goal]
            prefix_count[curr_sum] += 1
        return count
