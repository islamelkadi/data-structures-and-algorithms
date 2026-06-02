# 202. Happy Number

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/happy-number/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Hash set cycle detection applied to the digit-square-sum sequence.

## 2. How to Recognize the Pattern

- **Detect loop/cycle in a process**: "Determine if a number is happy (eventually reaches 1) or loops endlessly" indicates tracking history to detect cycles.
- **Finite state space**: Since the sum of squares of digits of any number reduces rapidly to a small range (e.g., under 243 for numbers up to 999), the sequence will either converge to 1 or repeat a value, which is a classic cycle detection problem.

## 3. Why This Algorithm Fits

- Each transition step is extremely fast ($O(\log N)$ to extract and sum digits).
- A hash set provides $O(1)$ lookup to check if a sum has been seen before, making cycle detection efficient.

## 4. How It Works

1. Initialize a hash set `seen_hashset` to store previously calculated values.
2. While $n \neq 1$:
   - Check if $n$ exists in `seen_hashset`. If so, we have entered a loop, so return `False`.
   - Add $n$ to `seen_hashset`.
   - Update $n$ to be the sum of the squares of its digits: `n = sum([int(x)**2 for x in str(n)])`.
3. If $n$ reaches 1, the `while` loop completes and we return `True`.

```python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        seen_hashset = set()
        while n != 1:
            if n in seen_hashset:
                return False
            seen_hashset.add(n)
            n = sum([int(x)**2 for x in str(n)])
        else:
            return True
```

### Dry Run Table
Input: `n = 19`

| n | digit squares | sum | in seen_hashset? | action |
|---|---|---|---|---|
| 19 | $1^2 + 9^2 = 1 + 81$ | 82 | no | Add 19 to set |
| 82 | $8^2 + 2^2 = 64 + 4$ | 68 | no | Add 82 to set |
| 68 | $6^2 + 8^2 = 36 + 64$ | 100 | no | Add 68 to set |
| 100 | $1^2 + 0^2 + 0^2 = 1$ | 1 | — | Loop ends $\to$ Return `True` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(\log N)$ where $N$ is the number `n`. Summing the squared digits of a number reduces its magnitude logarithmically. The number of steps in any cycle is also bounded by a small constant.
- **Space Complexity**: $O(\log N)$ to store the visited numbers in `seen_hashset`.
