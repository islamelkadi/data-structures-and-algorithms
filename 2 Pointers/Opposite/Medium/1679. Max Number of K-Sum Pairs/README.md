# 1679. Max Number of K-Sum Pairs

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/max-number-of-k-sum-pairs/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Sort + two pointers scanning inward to greedily find complement pairs that sum to k.

## 2. How to Recognize the Pattern

- "Two numbers that sum to k" + "remove them" + "maximize operations" → complement pair finding → sort then two-pointer scan.

## 3. Why This Algorithm Fits

- O(n log n) time — dominated by the sort; the two-pointer scan is O(n).
- O(1) space — sorting in-place, no extra storage.

## 4. How It Works

Sort the array so the smallest and largest values are at opposite ends. Use a left pointer at the start and a right pointer at the end. If their sum equals k, count the operation and move both pointers inward. If the sum is too small, advance left to increase it; if too large, retreat right to decrease it. Continue until the pointers meet.

```python
nums.sort()
left, right = 0, len(nums) - 1
count = 0
while left < right:
    s = nums[left] + nums[right]
    if s == k:
        count += 1; left += 1; right -= 1
    elif s < k:
        left += 1
    else:
        right -= 1
return count
```

Sorting first turns an unordered search into a directed one — each pointer move is guaranteed to bring the sum closer to k.

Input: `nums = [1, 2, 3, 4]`, `k = 5` (after sort: `[1, 2, 3, 4]`)

| left | right | nums[left] | nums[right] | sum | count | action |
|------|-------|------------|-------------|-----|-------|--------|
| 0 | 3 | 1 | 4 | 5 | 1 | ==k → count++, both move |
| 1 | 2 | 2 | 3 | 5 | 2 | ==k → count++, both move |
| 2 | 1 | — | — | — | 2 | left>=right → stop |
| result | | | | | 2 | |
