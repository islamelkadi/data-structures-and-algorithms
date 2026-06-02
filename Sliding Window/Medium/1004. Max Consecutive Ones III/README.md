# 1004. Max Consecutive Ones III
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/max-consecutive-ones-iii/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used
Variable-size sliding window with a "zero budget" of k; shrink when zeros in the window exceed k.

## 2. How to Recognize the Pattern
- "flip at most k zeros" + "longest subarray of 1s" → treat flipped zeros as a budget → variable sliding window.
- "at most k" constraint on a binary array → classic zero-budget window pattern.

## 3. Why This Algorithm Fits
- O(n) time — each element is visited at most twice (once by right, once by left).
- O(1) space — only a zero counter and two pointers.
- The window invariant is simple: count of zeros ≤ k.

## 4. How It Works

Expand right, counting zeros. When `zero_counter > k`, shrink from the left, decrementing the zero count when a zero leaves the window. The maximum valid window length is the answer.

```python
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zero_counter = max_subarray_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_counter += 1

            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1

            max_subarray_len = max(max_subarray_len, right - left + 1)
        return max_subarray_len
```

This is the general form of 1493 (Longest Subarray of 1s After Deleting One Element), which is just this problem with k=1 and a mandatory deletion.

Input: `nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]`, `k = 2`

| right | nums[right] | zero_counter | left | window size (valid) | max_subarray_len |
|-------|-------------|--------------|------|---------------------|------------------|
| 0-2   | 1, 1, 1     | 0            | 0    | 3                   | 3                |
| 3     | 0           | 1            | 0    | 4                   | 4                |
| 4     | 0           | 2            | 0    | 5                   | 5                |
| 5     | 0           | 3 > 2 → shrink| 4    | 2 (`[4, 5]`)        | 5                |
| 6-9   | 1, 1, 1, 1  | 2            | 4    | 6 (`[4, 9]`)        | 6                |
| 10    | 0           | 3 > 2 → shrink| 5    | 6 (`[5, 10]`)       | 6                |
| *end* | —           | —            | —    | —                   | 6                |
