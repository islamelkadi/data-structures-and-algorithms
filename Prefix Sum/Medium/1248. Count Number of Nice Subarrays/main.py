from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        curr = count = 0
        for num in nums:
            curr += num % 2
            count += prefix_count[curr - k]
            prefix_count[curr] += 1
        return count
