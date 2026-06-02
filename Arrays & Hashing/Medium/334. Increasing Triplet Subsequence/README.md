# 334. Increasing Triplet Subsequence

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/increasing-triplet-subsequence/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Greedy two-gate tracking.

## 2. How to Recognize the Pattern

- "Find three increasing values in order" → track the smallest possible pair so far, wait for a third to beat both.
- Brute force is O(n³). Greedy reduces it to O(n) by maintaining the lowest two gates — the smaller they are, the easier it is for a future number to clear both.
- No sorting allowed (order matters), no extra arrays needed — just two variables.

## 3. Why This Algorithm Fits

- Each number either lowers a gate or clears both — every element is handled in O(1).
- Greedy is safe because lowering a gate never invalidates a previous second gate. If `second_smallest` was set, there was a valid `smallest` before it — even if `smallest` has since moved.
- No need to remember the actual triplet — just whether one exists.

## 4. How It Works

Maintain two gates initialized to infinity. For each number:
- If it's ≤ the first gate, lower the first gate (new smallest).
- Else if it's ≤ the second gate, lower the second gate (it already passed gate 1).
- Else it passed both gates → triplet exists, return True.

```python
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = second_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num # lower the first gate
            elif num <= second_smallest:
                second_smallest = num   # lower the second gate (num already passed gate 1)
            else:
                return True # num passed both gates → triplet exists
        return False
```

Key subtlety: when `smallest` updates past `second_smallest` (e.g., smallest=5, second_smallest=12), it looks wrong. But `second_smallest = 12` guarantees a value smaller than 12 existed before it in the array. That forgotten value + 12 + current num forms the valid triplet.

### Dry Run Table
Input: `nums = [2, 1, 5, 0, 4, 6]`

| num | smallest | second_smallest | action |
|-----|----------|-----------------|--------|
| 2   | 2        | inf             | num ≤ smallest → lower gate 1 |
| 1   | 1        | inf             | num ≤ smallest → lower gate 1 |
| 5   | 1        | 5               | num > smallest, ≤ second → lower gate 2 |
| 0   | 0        | 5               | num ≤ smallest → lower gate 1 (5 still valid from before) |
| 4   | 0        | 4               | num > smallest, ≤ second → lower gate 2 |
| 6   | 0        | 4               | num > both gates → return True |

---

## 5. Time & Space Complexity

Time: O(n) — single pass, O(1) work per element.

Space: O(1) — only two variables.
