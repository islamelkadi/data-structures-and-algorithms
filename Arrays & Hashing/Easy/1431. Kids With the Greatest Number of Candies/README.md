# 1431. Kids With the Greatest Number of Candies

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm utilizes a linear scan with a precomputed maximum. First, we identify the current maximum value in the array. Then, we perform a second pass to compare each element (augmented by the extras) against this threshold.

## 2. How to Recognize the Pattern

- **Maximum/Threshold Comparisons**: The problem asks if a modification (adding `extraCandies`) can make each element the "greatest." This means we need to compare each element against a global maximum.
- **Single-Pass / Double-Pass Check**: Since we only need to compare against the largest value in the original array, we can find the maximum value in one pass and check the condition in a second pass, avoiding the need for nested comparisons or sorting.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ — Finding the maximum takes $O(N)$ time, and generating the boolean results array takes another $O(N)$ pass.
- **Space Complexity**: $O(1)$ auxiliary space, since we only maintain a single threshold variable (`max_no_extras`) and build the output array of size $N$ directly.

## 4. How It Works

1. Find the largest candy count without any extras: `max_no_extras = max(candies)`.
2. Initialize a list `max_candies` of size `len(candies)` with `False`.
3. Iterate through `candies` using their index:
   - If the current kid's candies + `extraCandies` meets or exceeds `max_no_extras`, set `max_candies[i] = True`.
4. Return `max_candies`.

```python
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_no_extras = max(candies)
        max_candies = [False] * len(candies)
        for i, kid_candy in enumerate(candies):
            if (kid_candy + extraCandies) >= max_no_extras:
                max_candies[i] = True
        return max_candies
```

### Dry Run Table
Input: `candies = [2, 3, 5, 1, 3]`, `extraCandies = 3`  
`max_no_extras = 5`

| Step/Index (`i`) | `candies[i]` | `candies[i] + 3` | Condition ($\ge 5$) | `max_candies` |
|------------------|--------------|------------------|---------------------|---------------|
| *init*           | —            | —                | —                   | `[False, False, False, False, False]` |
| 0                | 2            | 5                | `5 >= 5` (True)     | `[True, False, False, False, False]` |
| 1                | 3            | 6                | `6 >= 5` (True)     | `[True, True, False, False, False]` |
| 2                | 5            | 8                | `8 >= 5` (True)     | `[True, True, True, False, False]` |
| 3                | 1            | 4                | `4 >= 5` (False)    | `[True, True, True, False, False]` |
| 4                | 3            | 6                | `6 >= 5` (True)     | `[True, True, True, False, True]` |
