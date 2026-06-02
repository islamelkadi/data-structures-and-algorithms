# 2540. Minimum Common Value

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/minimum-common-value/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Two pointers converging on two sorted arrays to find the first common element.

## 2. How to Recognize the Pattern

- "Both arrays are sorted" + "find common element" → advance the smaller pointer → two-pointer linear scan.

## 3. Why This Algorithm Fits

- O(m + n) time — each pointer advances at most its array's length.
- O(1) space — no auxiliary data structure needed.

## 4. How It Works

Start both pointers at index 0. If the values match, return immediately — it's the minimum common value because both arrays are sorted. If nums1[i] is smaller, advance i to try to catch up to nums2[j]; otherwise advance j. If either pointer exits its array without a match, return -1.

```python
i, j = 0, 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        return nums1[i]
    elif nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1
return -1
```

The sorted property guarantees the first match found is the minimum — no need to scan further.

Input: `nums1 = [1, 2, 3]`, `nums2 = [2, 4]`

| i | j | nums1[i] | nums2[j] | action |
|---|---|----------|----------|--------|
| 0 | 0 | 1 | 2 | 1<2 → i++ |
| 1 | 0 | 2 | 2 | match → return 2 |
