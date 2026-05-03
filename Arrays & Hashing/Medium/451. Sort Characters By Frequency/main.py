# SORTING - BUCKET_SORT
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # Build frequency hashmap
        s_frequency_hashmap = Counter(s)

        # Build buckets
        buckets = [[] for _ in range(len(s) + 1)]

        # Populate buckets
        for char, frequency in s_frequency_hashmap.items():
            buckets[frequency].append(char * frequency)
        
        # Sort
        sorted_str_arr = []
        for i in range(len(buckets) - 1, -1, -1):
            sorted_str_arr.extend(buckets[i])
        return "".join(sorted_str_arr)