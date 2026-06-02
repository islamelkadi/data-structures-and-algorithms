# 451. Sort Characters By Frequency
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/sort-characters-by-frequency/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Bucket sort by character frequency: place each character's repeated string into a bucket indexed by its frequency, then concatenate buckets from highest to lowest.

## 2. How to Recognize the Pattern

- "sort characters by how often they appear" → rank by frequency → bucket sort on frequency.
- The maximum frequency of any character is the length of the string → bucket array of size n+1 is sufficient.
- Bucket sort avoids the O(n log n) cost of a comparison-based sort.

## 3. Why This Algorithm Fits

- O(n) time — one pass to build the Counter, one pass to fill buckets, one reverse pass to build the result.
- O(n) space — the Counter and bucket array together hold O(n) data.
- The same bucket-sort-by-frequency pattern used in Top K Frequent Elements (347) applies directly here.

## 4. How It Works

Build a `Counter` of all characters. Create a list of empty buckets indexed 0 through n. For each character and its frequency, append `char * frequency` (the character repeated frequency times) to the bucket at that index. Finally, iterate the bucket array from the end toward the front, collecting non-empty buckets, and join the result into a string.

```python
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
```

Storing `char * frequency` in the bucket rather than just the character means the final join step requires no additional repetition logic — the repeated string is already pre-built at insertion time.

Input: `s = "tree"`

| step | freq | buckets | result |
|------|------|---------|--------|
| count | {t:1, r:1, e:2} | | |
| fill | | [[], [], ["ee"], ["t","r"]] | |
| collect from end | | i=3→["t","r"], i=2→["ee"] | "tree" or "rtee" (order within bucket varies) |
