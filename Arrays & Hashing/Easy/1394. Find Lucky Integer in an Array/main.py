from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky = [x for x in freq if freq[x] == x]
        return max(lucky) if lucky else -1
