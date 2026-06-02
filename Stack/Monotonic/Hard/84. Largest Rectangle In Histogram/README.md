# 84. Largest Rectangle In Histogram

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/largest-rectangle-in-histogram/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Monotonic increasing stack (no padding variant).

## 2. How to Recognize the Pattern

- **Find maximum rectangular area in histogram**: We need to find how far each bar can extend left and right before hitting a shorter bar. Finding the nearest smaller element on both sides is a classic monotonic stack pattern.
- Same "next greater/smaller" element tracking pattern as Daily Temperatures, but applied here to compute rectangle widths.
- When you need to maximize a rectangular area under height constraints in a 1D array, think monotonic stack.

## 3. Why This Algorithm Fits

- The stack maintains bars in increasing height order. When a shorter bar arrives, all taller bars on the stack have found their right boundary — pop and compute area.
- The left boundary for any popped bar is the index of the bar remaining on top of the stack (the nearest shorter bar to the left).
- The flush loop at the end handles bars that never encountered a shorter bar to their right — their right boundary extends to the end of the array.
- An empty stack after a pop indicates the popped bar was the shortest bar seen so far; it can extend all the way to index 0, so `width = i` (or `len(heights)` during the flush loop).

## 4. How It Works

Push bars in increasing order. When a shorter bar arrives, pop taller bars and compute their area using:
- Right boundary: current index `i`
- Left boundary: `stack[-1]` index (nearest shorter bar to the left), or index 0 if stack is empty
- Width: `right - left - 1`, or just `i` if no left boundary exists

After the main loop, flush remaining bars using `len(heights)` as the right boundary.

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        for i, current_height in enumerate(heights):
            while stack and stack[-1][0] > current_height:
                popped_height, index = stack.pop()
                # You are doing a -1 (e.g. i - index - 1)
                # to get the left most boundary of the bar
                # that was just popped.

                # The stack[-1] represents the left boundary
                # which is the bar that hasn't been popped.
                width = i if not stack else i - stack[-1][-1] - 1
                max_area = max(max_area, popped_height * width)
            stack.append((current_height, i))
        
        while stack:
            popped_height, index = stack.pop()
            # Len of heights because your i is now equal to len(heights)
            # meaning you've done a complete first pass on the right side
            width = len(heights) if not stack else len(heights) - stack[-1][-1] - 1
            max_area = max(max_area, popped_height * width)
        return max_area
```

### Dry Run Table
Input: `heights = [2, 1, 5, 6, 2, 3]` (Length $N = 6$)

| Step / Index `i` | heights[i] | Stack State (before push) | Action | Popped `(height, idx)` | Width Calculation | Area | Max Area |
|---|---|---|---|---|---|---|---|
| *init* | — | `[]` | — | — | — | — | 0 |
| 0 | 2 | `[]` | Push | — | — | — | 0 |
| 1 | 1 | `[(2, 0)]` | Pop | `(2, 0)` | `1` (stack empty) | 2 | 2 |
| | | `[]` | Push | — | — | — | 2 |
| 2 | 5 | `[(1, 1)]` | Push | — | — | — | 2 |
| 3 | 6 | `[(1, 1), (5, 2)]` | Push | — | — | — | 2 |
| 4 | 2 | `[(1, 1), (5, 2), (6, 3)]`| Pop | `(6, 3)` | `4 - 2 - 1 = 1` | 6 | 6 |
| | | `[(1, 1), (5, 2)]` | Pop | `(5, 2)` | `4 - 1 - 1 = 2` | 10 | 10 |
| | | `[(1, 1)]` | Push | — | — | — | 10 |
| 5 | 3 | `[(1, 1), (2, 4)]` | Push | — | — | — | 10 |
| **Flush Loop** | — | `[(1, 1), (2, 4), (3, 5)]`| Pop | `(3, 5)` | `6 - 4 - 1 = 1` | 3 | 10 |
| | — | `[(1, 1), (2, 4)]` | Pop | `(2, 4)` | `6 - 1 - 1 = 4` | 8 | 10 |
| | — | `[(1, 1)]` | Pop | `(1, 1)` | `6` (stack empty) | 6 | 10 |
| *result* | — | `[]` | Finish | — | — | — | **10** |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `heights`. Each bar is pushed onto the stack once and popped off the stack once across the two loops.
- **Space Complexity**: $O(N)$ auxiliary space as the stack can hold at most $N$ elements in the case of strictly increasing heights.
