# 735. Asteroid Collision

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/asteroid-collision/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Stack-based collision simulation using a `while-else` construct to handle chain reactions.

## 2. How to Recognize the Pattern

- "Asteroids collide when moving in opposite directions" → process elements sequentially, undoing previous entries based on a condition → stack.
- The collision is always between the most recent right-moving asteroid and the incoming left-moving one → Last-In, First-Out (LIFO) behavior → stack.
- Similar to backspace or star elimination, but with three possible outcomes per collision: destroy incoming, destroy existing, or destroy both.

## 3. Why This Algorithm Fits

- The stack stores the surviving asteroids in order. An incoming left-moving asteroid (`asteroid < 0`) only collides with right-moving asteroids (`stack[-1] > 0`) at the top of the stack.
- A `while` loop handles chain reaction collisions: a single large left-moving asteroid can destroy multiple smaller right-moving ones on the stack until it meets its match or destroys them all.
- Python's `while-else` structure is exceptionally clean here: the `else` block executes only if the loop finishes without hitting a `break` statement (meaning the incoming asteroid survived all collisions and should be added to the stack).

## 4. How It Works

For each asteroid, check if it collides with the top of the stack (top is positive, incoming is negative). There are three collision outcomes:
- **Incoming is smaller**: The incoming asteroid is destroyed. Hit `break` to stop the loop and prevent it from being appended.
- **Equal size**: Both asteroids are destroyed. Call `pop()` to destroy the top of the stack, and hit `break` to prevent the incoming one from being appended.
- **Incoming is bigger**: The top of the stack is destroyed. Call `pop()` and continue the `while` loop to check for the next collision.

If the loop completes without a `break` (or if no collision condition was met), the `else` block triggers and appends the asteroid to the stack.

```python
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if abs(asteroids[i]) < abs(stack[-1]):
                    break
                if abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    break
                if abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
            else:
                stack.append(asteroids[i])
        return stack
```

### Dry Run Table
Input: `asteroids = [10, 2, -5]`

| Step | i | Asteroid | Stack State (before step) | Collision Check: `stack[-1] > 0 and ast < 0` | Action Taken | Stack State (after step) |
|------|---|----------|---------------------------|---------------------------------------------|--------------|--------------------------|
| *init*| - | -        | `[]`                      | -                                           | -            | `[]`                     |
| 0    | 0 | 10       | `[]`                      | No (empty)                                  | Append 10    | `[10]`                   |
| 1    | 1 | 2        | `[10]`                    | No (`2 > 0`)                                | Append 2     | `[10, 2]`                |
| 2    | 2 | -5       | `[10, 2]`                 | Yes (`2 > 0 and -5 < 0`)                    | `abs(-5) > abs(2)` $\to$ `pop(2)` | `[10]` |
|      |   |          | `[10]`                    | Yes (`10 > 0 and -5 < 0`)                   | `abs(-5) < abs(10)` $\to$ `break` | `[10]` |

Result: `[10]`

---

## 5. Time & Space Complexity

- **Time Complexity**: O(n) — each asteroid is pushed and popped at most once. The nested `while` loop amortizes to O(n) overall because the total number of pops cannot exceed the number of elements.
- **Space Complexity**: O(n) — for the stack, which holds up to n elements in the worst case (e.g., all moving in the same direction).
