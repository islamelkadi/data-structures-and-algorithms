# 125. Valid Palindrome

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/valid-palindrome/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Two-pointer inward comparison on a cleaned string.

## 2. How to Recognize the Pattern

- **Palindrome validation**: "Is it the same forwards and backwards?" represents a palindrome check, which is solved by comparing characters from both ends moving toward the middle.
- **Messy string cleaning**: The string contains non-alphanumeric characters and mixed case, so we clean it first before checking the palindrome properties.
- **Opposite direction pointers**: A classic $O(N)$ two-pointer approach where pointers move toward each other.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: One pass to clean the string, and one pass to compare the characters.
- **$O(N)$ space**: For storing the cleaned version of the string. (An $O(1)$ space approach is possible by skipping non-alphanumeric characters in-place, but pre-cleaning simplifies the logic).
- **Early termination**: We return `False` immediately upon the first character mismatch.

## 4. How It Works

Strip out everything that is not a letter or digit and convert the remaining string to lowercase. Place one pointer at the start and one at the end. Compare characters at both pointers — if they ever differ, return `False`. Move the pointers inward at each step. If the pointers meet without a mismatch, return `True`.

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(x.lower() for x in s if x.isalnum())
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

### Dry Run Table
Input: `s = "A man, a plan, a canal: Panama"` $\to$ cleaned: `"amanaplanacanalpanama"`

| left | right | s[left] | s[right] | action |
|---|---|---|---|---|
| 0 | 19 | a | a | match $\to$ move both |
| 1 | 18 | m | m | match $\to$ move both |
| 2 | 17 | a | a | match $\to$ move both |
| 3 | 16 | n | n | match $\to$ move both |
| 4 | 15 | a | a | match $\to$ move both |
| 5 | 14 | p | p | match $\to$ move both |
| 6 | 13 | l | l | match $\to$ move both |
| 7 | 12 | a | a | match $\to$ move both |
| 8 | 11 | n | n | match $\to$ move both |
| 9 | 10 | a | a | match $\to$ move both |
| 10 | 9 | — | — | `left >= right` $\to$ stop, return `True` |

Result: `True`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of characters in the string `s`. Cleaning the string takes $O(N)$ time, and the two-pointer traversal makes at most $N/2$ comparisons, which is also $O(N)$.
- **Space Complexity**: $O(N)$ space to store the cleaned string.
