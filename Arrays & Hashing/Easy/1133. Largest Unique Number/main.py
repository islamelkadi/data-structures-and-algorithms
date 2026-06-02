from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Using hashmap
        max_val = -1
        occurrences = Counter(nums)
        
        for key, val in occurrences.items():
            if val != 1:
                continue
            
            max_val = max(max_val, key)
        return max_val
