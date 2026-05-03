from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = curr = 0
        for g in gain:
            curr += g
            max_alt = max(max_alt, curr)
        return max_alt
