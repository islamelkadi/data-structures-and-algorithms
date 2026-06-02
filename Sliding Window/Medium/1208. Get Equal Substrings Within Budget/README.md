# 1208. Get Equal Substrings Within Budget
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/get-equal-substrings-within-budget/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used
Variable-size sliding window where cost = sum of |s[i] - t[i]|; shrink when cost exceeds maxCost.

## 2. How to Recognize the Pattern
- "change characters to make equal" + "budget constraint" + "longest substring" → per-position cost with a total budget → variable sliding window.
- The cost of a window is the sum of individual character-change costs, which is additive and easy to maintain incrementally.

## 3. Why This Algorithm Fits
- O(n) time — single pass with two pointers.
- O(1) space — only a running cost and two pointers.
- Per-position costs are independent, so adding/removing an element from the window updates the total cost in O(1).

## 4. How It Works
Compute the cost of adding `s[right]`/`t[right]` to the window. If `curr > maxCost`, subtract the cost of the leftmost position and advance `left`. Track the maximum valid window length.

```python
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = curr = ans = 0
        for right in range(len(s)):
            curr += abs(ord(s[right]) - ord(t[right]))
            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

`ord(c)` converts a character to its ASCII value; the absolute difference gives the minimum cost to change one character to the other.

Input: `s = "abcd"`, `t = "bcdf"`, `maxCost = 3`

| right | s[r] | t[r] | cost added | curr (total cost) | left | window size | ans |
|-------|------|------|------------|-------------------|------|-------------|-----|
| 0 | a | b | 1 | 1 | 0 | 1 | 1 |
| 1 | b | c | 1 | 2 | 0 | 2 | 2 |
| 2 | c | d | 1 | 3 | 0 | 3 | 3 |
| 3 | d | f | 2 | 5 > 3 → shrink | 1 | 3 | 3 |
