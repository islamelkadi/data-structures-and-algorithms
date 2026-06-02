# 151. Reverse Words in a String

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/reverse-words-in-a-string/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Split, two-pointer reversal, rejoin.

## 2. How to Recognize the Pattern

- **Reverse the order of words**: Indicates reversing a list, which maps to two pointers swapping elements from both ends.
- **Messy whitespace**: Splitting with `split()` (no arguments) handles multiple adjacent spaces and leading/trailing whitespace automatically.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Splitting is $O(N)$, reversal is $O(W)$ (where $W$ is the number of words), and joining is $O(N)$.
- **$O(N)$ space**: Required for storing the list of words.
- `split()` does the heavy lifting of cleaning up whitespace, so the reversal logic stays simple and clean.

## 4. How It Works

Split the string into a list of words (whitespace handled automatically). Use two pointers to swap words from the outside in. Join with a single space.

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return " ".join(s)
```

Worth noting: `s.split()` + `" ".join(s)` already handles the tricky parts of this problem (extra spaces, leading/trailing spaces). The two-pointer swap is equivalent to `s[::-1]` or `s.reverse()`, so you could also just do `return " ".join(s.split()[::-1])` — but the explicit pointer approach is better for interviews since it shows you understand the mechanics.

### Dry Run Table
Input: `s = "  the sky  is blue  "`

| step | action | state |
|---|---|---|
| split | `s.split()` | `["the", "sky", "is", "blue"]` |
| left=0, right=3 | swap "the" $\leftrightarrow$ "blue" | `["blue", "sky", "is", "the"]` |
| left=1, right=2 | swap "sky" $\leftrightarrow$ "is" | `["blue", "is", "sky", "the"]` |
| left=2, right=1 | `left >= right` $\to$ stop | — |
| join | `" ".join(...)` | `"blue is sky the"` |

Result: `"blue is sky the"`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of string `s`. Splitting takes $O(N)$, the two-pointer swap runs in $O(W)$ (where $W \le N$ is the number of words), and joining the words takes $O(N)$ time.
- **Space Complexity**: $O(N)$ to hold the split list of words.
