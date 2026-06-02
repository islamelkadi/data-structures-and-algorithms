# 1394. Find Lucky Integer in an Array
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/find-lucky-integer-in-an-array/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Frequency map — find the maximum element whose value equals its frequency.

## 2. How to Recognize the Pattern

- "find element where value equals its count" → build a frequency map → filter where freq[x] == x.
- "return the largest" → take max of the filtered list, or -1 if empty.

## 3. Why This Algorithm Fits

- O(n) time — one pass to build the counter, one pass to filter.
- O(k) space — k is the number of distinct elements.
- Counter makes the frequency lookup O(1) per element.

## 4. How It Works

Count the frequency of each element. Collect all elements x where the frequency equals x itself. Return the maximum of those, or -1 if none exist.

```python
from typing import List
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky = [x for x in freq if freq[x] == x]
        return max(lucky) if lucky else -1
```

The condition `freq[x] == x` directly encodes the definition of a lucky number — the value and its occurrence count are the same.

Input: `arr = [2, 2, 3, 4]`

| step | freq | lucky candidates | result |
|------|------|-----------------|--------|
| build | {2:2, 3:1, 4:1} | x=2: freq[2]==2 ✓ | max([2]) = 2 |
