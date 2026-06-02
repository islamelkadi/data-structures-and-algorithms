# 1748. Sum of Unique Elements
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/sum-of-unique-elements/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Frequency map — sum only the elements that appear exactly once.

## 2. How to Recognize the Pattern

- "sum elements that appear only once" → build a frequency map → filter by count == 1.
- Any problem asking to distinguish unique from repeated elements maps to a Counter.

## 3. Why This Algorithm Fits

- O(n) time — one pass to count, one pass to sum.
- O(k) space — k is the number of distinct elements.
- Counter's O(1) lookup makes the filter step efficient.

## 4. How It Works

Count the frequency of each element. Sum all elements whose frequency is exactly 1.

```python
from typing import List
from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum(x for x in freq if freq[x] == 1)
```

Iterating over `freq` (the keys) rather than `nums` avoids double-counting — each unique element is visited once regardless of how many times it appears in the original array.

Input: `nums = [1, 2, 3, 2]`

| step | freq | filter (freq==1) | sum |
|------|------|-----------------|-----|
| build | {1:1, 2:2, 3:1} | [1, 3] | 4 |
