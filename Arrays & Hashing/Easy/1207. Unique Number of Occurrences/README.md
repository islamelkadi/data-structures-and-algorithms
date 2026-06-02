# 1207. Unique Number of Occurrences
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/unique-number-of-occurrences/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Frequency map with a uniqueness check on the frequency values using a set.

## 2. How to Recognize the Pattern

- "check if occurrence counts are all different" → build a frequency map → compare value count to set size.
- If converting the frequency values to a set reduces the count, there are duplicates.

## 3. Why This Algorithm Fits

- O(n) time — one pass to build the counter, one pass to build the set.
- O(k) space — k is the number of distinct elements.
- Set size vs dict size comparison is a clean O(1) uniqueness check.

## 4. How It Works

Count the frequency of each element with a Counter. Iterating over the frequencies, keep track of seen frequencies in a set. If a frequency is already in the set, return `False`. If the loop finishes without duplicates, return `True`.

```python
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
```

The loop iterates over the frequency values and uses the `seen_hashset` for early exit upon detecting any duplicate frequency.

Input: `arr = [1, 2, 2, 1, 1, 3]`
Frequencies: `{1: 3, 2: 2, 3: 1}`

| freq | seen_hashset | Condition: `freq in seen_hashset` | Action Taken |
|------|--------------|----------------------------------|--------------|
| *init*| `set()`      | -                                | -            |
| 3    | `{3}`        | `3 in set()` → False             | Add 3 to set |
| 2    | `{3, 2}`     | `2 in {3}` → False               | Add 2 to set |
| 1    | `{3, 2, 1}`  | `1 in {3, 2}` → False            | Add 1 to set |
| *end*| `{3, 2, 1}`  | -                                | Return True  |
