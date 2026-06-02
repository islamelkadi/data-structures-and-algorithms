# 1133. Largest Unique Number

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/largest-unique-number/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

HashMap / Frequency counting with Counter to track number occurrences, followed by a linear scan of unique keys to find the maximum.

## 2. How to Recognize the Pattern

- "find the largest integer that only occurs once" → check frequency of each element → frequency map / hash map.
- Uniqueness is checked by occurrences equal to 1, and among those, we need to track the maximum element.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(N) where N is the length of `nums` to populate the `Counter` and iterate over unique values.
- **Space Complexity**: O(K) where K is the number of unique elements in `nums` (bounded by N) to store occurrences in the hash map.
- The lookup and insert operations are O(1), making frequency mapping optimal.

## 4. How It Works

1. Build a frequency count of each integer in `nums` using a `Counter`.
2. Initialize `max_val` to `-1` to handle the edge case where no unique integer exists.
3. Iterate through the unique key-value pairs in the frequency map:
   - If the value (frequency) is equal to 1, compare the key (element) with `max_val` and record the larger one.
4. Return `max_val`.

```python
from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        max_val = -1
        occurrences = Counter(nums)
        
        for key, val in occurrences.items():
            if val != 1:
                continue
            
            max_val = max(max_val, key)
        return max_val
```

### Dry Run Table
Input: `nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]`

`occurrences`: `{5: 1, 7: 1, 3: 2, 9: 2, 4: 1, 8: 1, 1: 1}`

| key | val | val != 1? | max_val comparison | max_val |
|-----|-----|-----------|--------------------|---------|
| *init* | - | - | - | -1 |
| 5 | 1 | False | `max(-1, 5) = 5` | 5 |
| 7 | 1 | False | `max(5, 7) = 7` | 7 |
| 3 | 2 | True | Skip | 7 |
| 9 | 2 | True | Skip | 7 |
| 4 | 1 | False | `max(7, 4) = 7` | 7 |
| 8 | 1 | False | `max(7, 8) = 8` | 8 |
| 1 | 1 | False | `max(8, 1) = 8` | 8 |

Result: `8`
