
# SLIDING WINDOW
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create frequency tracker
        nums_frequency = Counter(nums)

        # Create empty buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Populate buckets
        for num, frequency in nums_frequency.items():
            # Frequency here serves as the index
            buckets[frequency].append(num)
        
        # You are starting from the end because 
        # bucket sort puts the most frequent items
        # at the end 
        output = []
        for i in range(len(buckets) - 1, -1, -1):
            output.extend(buckets[i])
            if len(output) >= k:
                return output