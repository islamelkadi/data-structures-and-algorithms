# 392. Is Subsequence

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/is-subsequence/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Single-pointer greedy scan with slow pointer

## 2. How to Recognize the Pattern

- "Is s a subsequence of t?" → characters of s must appear in t in order, but not necessarily contiguously.
- You're matching one sequence against another in order → single pointer on s, iterate through t.
- Greedy works because the earliest match is always the best choice — it leaves the most room for future matches.

## 3. Why This Algorithm Fits

- One pass through t is enough — no need for backtracking or dynamic programming.
- The pointer on s only advances on a match, naturally preserving order.
- Early return when all characters are matched avoids scanning the rest of t.

## 4. How It Works

Keep a pointer on s starting at 0. Walk through every character in t. When a character matches `s[slow_pointer]`, advance the pointer. If the pointer reaches the end of s, all characters were found in order — return True. If you finish t without matching all of s, return False.

```python
if len(s) > len(t):
    return False
if not s:
    return True

slow_pointer = 0
for char in t:
    if char == s[slow_pointer]:
        slow_pointer += 1
    if slow_pointer == len(s):
        return True
return False
```

### Dry Run Table
Input: `s = "ace"`, `t = "abcde"`

| char (t) | s[slow_pointer] | match? | slow_pointer |
|----------|-----------------|--------|--------------|
| a        | a               | yes    | 1            |
| b        | c               | no     | 1            |
| c        | c               | yes    | 2            |
| d        | e               | no     | 2            |
| e        | e               | yes    | 3 = len(s) → return True |

---

## 5. Time & Space Complexity

Time: O(n) where n is the length of t — single pass through t, each comparison is O(1).

Space: O(1) — only a single pointer variable, no extra data structures.
