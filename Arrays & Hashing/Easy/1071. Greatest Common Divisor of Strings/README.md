# 1071. Greatest Common Divisor of Strings

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/greatest-common-divisor-of-strings/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Euclidean algorithm (GCD) applied to string lengths, coupled with a concatenation check to verify string periodicity.

## 2. How to Recognize the Pattern

- Anytime a problem mentions "divisor", "divides evenly", or "repeating pattern" → think GCD.
- If two sequences are built from the same repeating unit, the largest common unit's size is the GCD of the two sizes. This applies to strings, arrays, or periodic cycles.
- The concatenation trick (`str1 + str2 == str2 + str1`) checks if two strings share a common repeating base. If order of concatenation does not matter, they are made of the same repeating block.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(n + m) — The concatenation check takes O(n + m) time, and the Euclidean algorithm takes O(log(min(n, m))) time.
- **Space Complexity**: O(n + m) — Needed to store the concatenated strings for comparison.
- Once it is verified that a common base block exists, the length of the greatest common divisor is mathematically guaranteed to be `gcd(len(str1), len(str2))`.

## 4. How It Works

1. Compare `str1 + str2` with `str2 + str1`. If they are not equal, a common divisor string is impossible; return `""`.
2. Compute the GCD of the lengths of `str1` and `str2` using the Euclidean algorithm:
   - Repeatedly perform `s, t = t, s % t` until `t` is `0`.
3. Return the substring of `str1` of length `s`. Note that taking `str1[-s:]` or `str1[:s]` yields the same result because of the periodic structure.

```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""

        s, t = len(str1), len(str2)
        while t:
            s, t = t, s % t
        
        return str1[-s:]
```

### Dry Run Table
Input: `str1 = "ABCABC"`, `str2 = "ABC"`

- **Concatenation Check**: `"ABCABC" + "ABC"` $\to$ `"ABCABCABC"` vs `"ABC" + "ABCABC"` $\to$ `"ABCABCABC"` (Equal $\to$ Proceed)

**Euclidean Algorithm (`s = 6`, `t = 3`):**

| Step | s | t | Loop Condition `t != 0` | Next state (`s, t = t, s % t`) | Action / Result |
|------|---|---|-------------------------|--------------------------------|-----------------|
| *init*| 6 | 3 | -                       | -                              | -               |
| 1    | 6 | 3 | True                    | `s = 3`, `t = 6 % 3 = 0`       | Continue        |
| 2    | 3 | 0 | False                   | -                              | Loop terminates |

- **Result**: `str1[-3:]` $\to$ `"ABC"`
