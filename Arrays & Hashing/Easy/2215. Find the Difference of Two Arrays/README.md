# 2215. Find the Difference of Two Arrays
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/find-the-difference-of-two-arrays/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Set difference in both directions to find elements unique to each array.

## 2. How to Recognize the Pattern

- "elements in A not in B, and elements in B not in A" → set difference → `s1 - s2` and `s2 - s1`.
- Duplicates don't matter for membership — converting to sets handles that automatically.

## 3. Why This Algorithm Fits

- O(n + m) time — converting both arrays to sets and computing differences are all linear.
- O(n + m) space — storing both sets.
- Set difference is a built-in O(n) operation in Python.

## 4. How It Works

Convert both arrays to sets to eliminate duplicates and enable O(1) membership checks. Use Python's set subtraction operator to find elements exclusive to each side.

```python
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
```

`s1 - s2` gives all elements in s1 that are not in s2, and vice versa — exactly what the problem asks for.

Input: `nums1 = [1,2,3]`, `nums2 = [2,4,6]`

| step | s1 | s2 | s1-s2 | s2-s1 |
|------|----|----|-------|-------|
| convert | {1,2,3} | {2,4,6} | {1,3} | {4,6} |
| result | | | [1,3] | [4,6] |
