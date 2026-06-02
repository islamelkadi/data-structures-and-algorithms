# 28. Find the Index of the First Occurrence in a String

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Sliding window substring comparison (brute force).

## 2. How to Recognize the Pattern

- **Find the first occurrence of a substring**: Slide a window of `needle`'s length across `haystack` and compare.
- **Fixed window size**: The window size is fixed at `len(needle)`.
- While more advanced pattern-matching algorithms exist (like KMP or Rabin-Karp), this straightforward brute force sliding window is highly clean, easy to read, and widely accepted.

## 3. Why This Algorithm Fits

- Simple and highly readable — a single loop with one comparison per position.
- Python's string slicing and built-in equality checking handle comparison details cleanly.
- No out-of-bounds edge case issues: if `needle` is longer than the remaining part of `haystack`, the slice is simply shorter and will not match.

## 4. How It Works

Slide through `haystack` one character at a time. At each index `i`, extract a slice of length `len(needle)` and compare it to `needle`. Return `i` on the first match. If the loop completes with no match, return `-1`.

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
```

### Dry Run Table
Input: `haystack = "sadbutsad"`, `needle = "sad"`

| i | Haystack Slice `haystack[i:i+len(needle)]` | Equals `needle`? | Action |
|---|---|---|---|
| 0 | `"sad"` | yes | Return `0` |

Result: `0`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N \cdot M)$ where $N$ is the length of `haystack` and $M$ is the length of `needle`. In the worst case, we perform a comparison of cost $O(M)$ at each of the $N$ index positions.
- **Space Complexity**: $O(M)$ auxiliary space since the string slice operation allocates a new string of length $M$ at each step.
