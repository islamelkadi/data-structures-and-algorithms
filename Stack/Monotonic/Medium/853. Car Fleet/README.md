# 853. Car Fleet

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/car-fleet/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Monotonic stack with time-to-target calculation.

## 2. How to Recognize the Pattern

- "How many groups arrive together?" → cars that catch up merge into fleets → monotonic stack.
- Sorting by position (closest to target first) lets you process cars in the order they'd encounter each other.
- A slower car (higher arrival time) blocks faster cars behind it → only push when a car is slower than the fleet ahead.

## 3. Why This Algorithm Fits

- After sorting by position descending, each car only needs to compare against the fleet directly ahead (top of stack).
- If a car arrives faster (less or equal time) than the fleet ahead, it merges — don't push.
- If it's slower (more time), it forms a new fleet — push it.
- The stack ends up holding one entry per fleet.

## 4. How It Works

Pair positions with speeds, sort by position descending (closest to target first). For each car, calculate time to reach target. If it's slower than the fleet ahead (top of stack), it's a new fleet — push. Otherwise it merges — skip.

```python
class Solution(object):
    def carFleet(self, target, position, speed):
        zipped_positions_speed = [(x1, x2) for x1, x2 in zip(position, speed)]
        zipped_positions_speed.sort(reverse=True)
        stack = []
        for car in zipped_positions_speed:
            current_time = (target - car[0]) / float(car[-1])
            if not stack or current_time > stack[-1]:
                stack.append(current_time)
        return len(stack)
```

Python 2 gotcha: `/ float(car[-1])` ensures float division. Without it, `4 / 3 = 1` in Python 2 instead of `1.333`.

### Dry Run Table
Input: `target = 12`, `position = [10, 8, 0, 5, 3]`, `speed = [2, 4, 1, 1, 3]`
*Sorted by position descending*: `[(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]`

| Step / Car | Position | Speed | Time to Target `(target - pos) / speed` | Stack Top `stack[-1]` | Check: `time > stack[-1]`? | Action | Stack State | Fleets (Stack Size) |
|------------|----------|-------|----------------------------------------|-----------------------|----------------------------|--------|-------------|---------------------|
| *init*     | —        | —     | —                                      | —                     | —                          | —      | `[]`        | 0                   |
| 1          | 10       | 2     | `(12 - 10) / 2 = 1.0`                  | — (empty)             | — (always push first)      | Push   | `[1.0]`     | 1                   |
| 2          | 8        | 4     | `(12 - 8) / 4 = 1.0`                   | 1.0                   | `1.0 > 1.0` (False)        | Merge  | `[1.0]`     | 1                   |
| 3          | 5        | 1     | `(12 - 5) / 1 = 7.0`                   | 1.0                   | `7.0 > 1.0` (True)         | Push   | `[1.0, 7.0]`| 2                   |
| 4          | 3        | 3     | `(12 - 3) / 3 = 3.0`                   | 7.0                   | `3.0 > 7.0` (False)        | Merge  | `[1.0, 7.0]`| 2                   |
| 5          | 0        | 1     | `(12 - 0) / 1 = 12.0`                  | 7.0                   | `12.0 > 7.0` (True)        | Push   | `[1.0, 7.0, 12.0]` | 3            |
| *result*   | —        | —     | —                                      | —                     | —                          | Finish | —           | **3**               |

---

## 5. Time & Space Complexity

- **Time Complexity**: O(n log n) — sorting dominates. The stack loop is O(n) since each car is visited once with no popping.
- **Space Complexity**: O(n) — for the zipped list and the stack.
