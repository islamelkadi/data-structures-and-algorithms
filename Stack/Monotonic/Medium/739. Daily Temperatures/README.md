# 739. Daily Temperatures

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/daily-temperatures/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Monotonic decreasing stack.

## 2. How to Recognize the Pattern

- "How many days until a warmer temperature?" → for each element, find the next greater element → monotonic stack.
- Anytime you need "next greater/smaller element" for every item in an array, think monotonic stack.
- Brute force is O(n²) — for each day, scan forward. The stack processes each element at most twice (push + pop), giving O(n).

## 3. Why This Algorithm Fits

- The stack maintains a decreasing sequence of temperatures. When a warmer day arrives, it resolves all cooler days waiting on the stack.
- Each day is pushed once and popped once — no redundant comparisons.
- Days that never find a warmer temperature stay on the stack and keep their default value of 0.

## 4. How It Works

Walk through temperatures. For each day, while the stack's top is cooler than today, pop it — today is the answer for that popped day. Record the distance (`i - index`). Then push today onto the stack.

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        temperature_tracker = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                _, index = stack.pop()
                temperature_tracker[index] = i - index
            stack.append((temperatures[i], i))
        return temperature_tracker
```

### Dry Run Table
Input: `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`

| Step / Index `i` | Temp | Stack State (before check) | Action | Popped `(temp, idx)` | Distance `i - idx` | `tracker` State | Stack State (after step) |
|---|---|---|---|---|---|---|---|
| *init* | — | `[]` | — | — | — | `[0, 0, 0, 0, 0, 0, 0, 0]` | `[]` |
| 0 | 73 | `[]` | Push | — | — | `[0, 0, 0, 0, 0, 0, 0, 0]` | `[(73, 0)]` |
| 1 | 74 | `[(73, 0)]` | Pop | `(73, 0)` | `1 - 0 = 1` | `[1, 0, 0, 0, 0, 0, 0, 0]` | `[]` |
| | | `[]` | Push | — | — | `[1, 0, 0, 0, 0, 0, 0, 0]` | `[(74, 1)]` |
| 2 | 75 | `[(74, 1)]` | Pop | `(74, 1)` | `2 - 1 = 1` | `[1, 1, 0, 0, 0, 0, 0, 0]` | `[]` |
| | | `[]` | Push | — | — | `[1, 1, 0, 0, 0, 0, 0, 0]` | `[(75, 2)]` |
| 3 | 71 | `[(75, 2)]` | Push | — | — | `[1, 1, 0, 0, 0, 0, 0, 0]` | `[(75, 2), (71, 3)]` |
| 4 | 69 | `[(75, 2), (71, 3)]` | Push | — | — | `[1, 1, 0, 0, 0, 0, 0, 0]` | `[(75, 2), (71, 3), (69, 4)]` |
| 5 | 72 | `[(75, 2), (71, 3), (69, 4)]` | Pop | `(69, 4)` | `5 - 4 = 1` | `[1, 1, 0, 0, 1, 0, 0, 0]` | `[(75, 2), (71, 3)]` |
| | | `[(75, 2), (71, 3)]` | Pop | `(71, 3)` | `5 - 3 = 2` | `[1, 1, 0, 2, 1, 0, 0, 0]` | `[(75, 2)]` |
| | | `[(75, 2)]` | Push | — | — | `[1, 1, 0, 2, 1, 0, 0, 0]` | `[(75, 2), (72, 5)]` |
| 6 | 76 | `[(75, 2), (72, 5)]` | Pop | `(72, 5)` | `6 - 5 = 1` | `[1, 1, 0, 2, 1, 1, 0, 0]` | `[(75, 2)]` |
| | | `[(75, 2)]` | Pop | `(75, 2)` | `6 - 2 = 4` | `[1, 1, 4, 2, 1, 1, 0, 0]` | `[]` |
| | | `[]` | Push | — | — | `[1, 1, 4, 2, 1, 1, 0, 0]` | `[(76, 6)]` |
| 7 | 73 | `[(76, 6)]` | Push | — | — | `[1, 1, 4, 2, 1, 1, 0, 0]` | `[(76, 6), (73, 7)]` |
| *result* | — | `[(76, 6), (73, 7)]` | Finish | — | — | `[1, 1, 4, 2, 1, 1, 0, 0]` | — |

---

## 5. Time & Space Complexity

- **Time Complexity**: O(n) — each element is pushed and popped at most once. The while loop across all iterations does at most n pops total.
- **Space Complexity**: O(n) — the stack holds at most n elements (if temperatures are strictly decreasing), plus the output array.
