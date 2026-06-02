from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequencies = Counter(arr)
        seen_hashset = set()

        for freq in frequencies.values():
            if freq in seen_hashset:
                return False
            seen_hashset.add(freq)
        return True
