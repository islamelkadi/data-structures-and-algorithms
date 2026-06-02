from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        max_frequency = max(frequency.values())
        
        total_occurrence = 0
        for i in frequency.values():
            if i == max_frequency:
                total_occurrence += i
        return total_occurrence
