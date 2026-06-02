# 1470. Shuffle the Array

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/shuffle-the-array/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm utilizes a two-pointer interleaved traversal (implemented with a single shared index). It walks through the first half of the array and the second half of the array simultaneously, appending elements alternately to form the shuffled result.

## 2. How to Recognize the Pattern

- **Alternating / Interleaving Subarrays**: The problem asks to shuffle an array of size $2n$ from `[x1, x2, ..., xn, y1, y2, ..., yn]` into `[x1, y1, x2, y2, ..., xn, yn]`. This is a classic pattern of merging two halves in alternating sequence.
- **Synchronized Traversal**: Since we take exactly one element from the first half and one element from the second half at each step, both traversal pointers move at the same rate. This allows us to use a single loop index `i` to represent the first pointer (`i`) and the second pointer (`i + n`).

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ — We iterate $N$ times, visiting each of the $2N$ elements exactly once.
- **Space Complexity**: $O(N)$ (or $O(2N)$) — The output array is constructed using space proportional to the input size.

## 4. How It Works

1. Initialize an empty list `new`.
2. Iterate `i` from `0` to `n - 1`.
3. At each iteration, append `nums[i]` (from the first half) and `nums[i + n]` (from the second half) to `new`.
4. Return `new`.

```python
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new = []
        for i in range(n):
            new += ([nums[i], nums[i+n]])
        return new
```

### Dry Run Table
Input: `nums = [2, 5, 1, 3, 4, 7]`, `n = 3`

| Step/Index (`i`) | `nums[i]` | `nums[i+n]` | `new` | Action Taken |
|------------------|-----------|-------------|-------|--------------|
| *init*           | —         | —           | `[]`  | Start loop from `i = 0` to `2` |
| 0                | 2 (index 0)| 3 (index 3)| `[2, 3]` | Append `nums[0]` and `nums[3]` |
| 1                | 5 (index 1)| 4 (index 4)| `[2, 3, 5, 4]` | Append `nums[1]` and `nums[4]` |
| 2                | 1 (index 2)| 7 (index 5)| `[2, 3, 5, 4, 1, 7]` | Append `nums[2]` and `nums[5]` |
