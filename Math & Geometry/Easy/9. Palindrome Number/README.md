# 9. Palindrome Number

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/palindrome-number/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Numerical integer reversal using modulo (`%`) and integer division (`//`) arithmetic.

## 2. How to Recognize the Pattern

- **Validate if an integer is a palindrome without string conversion**: Suggests reversing the digits of the number mathematically and comparing it with the original number.
- **Negative numbers constraint**: Any negative integer is immediately invalid because the leading negative sign (`-`) cannot match any digit at the end of the number.

## 3. Why This Algorithm Fits

- **$O(\log_{10} X)$ time**: The number of digits in $X$ is proportional to $\log_{10}(X)$. We divide the number by 10 in each loop iteration, achieving logarithmic time.
- **$O(1)$ space**: Runs using only two integer tracking variables, avoiding the $O(\log X)$ string allocation space of `str(x)`.

## 4. How It Works

1. If $x < 0$, return `False` immediately.
2. Initialize `x_2 = x` (to preserve the original number) and `rev = 0` (to build the reversed number).
3. While `x_2 > 0`:
   - Get the last digit of `x_2` using `x_2 % 10`.
   - Shift `rev` left by multiplying by 10, then add the extracted digit.
   - Truncate the last digit of `x_2` using floor division (`x_2 //= 10`).
4. Return whether `x == rev`.

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_2 = x
            rev = 0
            while x_2 > 0:
                rev = x_2 % 10 + rev * 10
                x_2 //= 10
            return x == rev
```

### Dry Run Table
Input: `x = 121`

*Initial State:* `x_2 = 121`, `rev = 0`

| Iteration | x_2 | last digit (`x_2 % 10`) | new rev (`rev * 10 + digit`) | new x_2 (`x_2 // 10`) |
|---|---|---|---|---|
| 1 | 121 | 1 | $0 \times 10 + 1 = 1$ | 12 |
| 2 | 12 | 2 | $1 \times 10 + 2 = 12$ | 1 |
| 3 | 1 | 1 | $12 \times 10 + 1 = 121$ | 0 |

Loop terminates as `x_2 == 0`. Check: `x == rev` ($121 == 121$) $\to$ `True`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(\log_{10} X)$ where $X$ is the value of the input integer `x`. The loop runs once for every decimal digit of $X$.
- **Space Complexity**: $O(1)$ auxiliary space as we only use two integer variables.
