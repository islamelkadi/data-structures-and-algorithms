# 70. Climbing Stairs

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/climbing-stairs/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Fibonacci sequence via iterative space optimization.

## 2. How to Recognize the Pattern

- **Climbing stairs taking 1 or 2 steps**: To reach step $n$, you must come from either step $n-1$ or step $n-2$. This gives the recurrence relation: $dp[n] = dp[n-1] + dp[n-2]$, which is the Fibonacci sequence.
- **Count distinct ways to reach a target**: Any problem asking for the number of distinct ways to reach a state using a set of fixed-sized steps represents a counting dynamic programming problem.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Requires a single iteration up to $n$.
- **$O(1)$ space**: Since the state at step $n$ only depends on the previous two steps, we can optimize space by tracking only the last two values (`a` and `b`) instead of maintaining a full DP table of size $n$.

## 4. How It Works

We initialize `a = 1` (representing the ways to reach step 0) and `b = 0` (representing step -1).
For each iteration up to $n$:
1. The new value of `a` becomes the sum of the current `a` and `b`.
2. The new value of `b` becomes the old value of `a`.

At the end of $n$ iterations, `a` contains the total number of distinct ways to climb the stairs.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 0
        for _ in range(n):
            a, b = a + b, a
        return a
```

### Dry Run Table
Input: `n = 4`

Initial state: `a = 1`, `b = 0`

| Iteration | a (before update) | b (before update) | a (after update: a + b) | b (after update: old a) |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 2 | 1 |
| 3 | 2 | 1 | 3 | 2 |
| 4 | 3 | 2 | 5 | 3 |

Result: `5`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of stairs `n`. We run a loop of size $N$.
- **Space Complexity**: $O(1)$ auxiliary space as we only use two tracking variables (`a` and `b`).
