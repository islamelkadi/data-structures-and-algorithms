# 54. Spiral Matrix

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/spiral-matrix/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)
6. [6. Mistakes & Lessons Learned](#6-mistakes--lessons-learned)

## 1. Algorithm Used

Four-boundary pointer traversal (top, bottom, left, right) with inline boundary checks.

## 2. How to Recognize the Pattern

- **Spiral traversal of a grid**: Rotate and descend through matrix dimensions by shifting pointer boundaries inwards (`top += 1`, `right -= 1`, `bottom -= 1`, `left += 1`).
- **Edge cases with non-square matrices**: Rectangular dimensions (`M != N`) mean that during an iteration, you can run out of rows or columns before completing all four directional passes.

## 3. Why This Algorithm Fits

- **$O(M \times N)$ time**: Each element in the grid is visited exactly once.
- **$O(1)$ space**: Modifies nothing and allocates no auxiliary matrices; we only maintain boundary integers.

## 4. How It Works

We maintain four pointers: `top = 0`, `bottom = len(matrix)`, `left = 0`, and `right = len(matrix[0])`. While `top < bottom and left < right`:
1. Traverse from `left` to `right` along the `top` row, then increment `top`.
2. Traverse from `top` to `bottom` along the `right` column, then decrement `right`.
3. Check if `top < bottom`. If so, traverse from `right - 1` to `left - 1` along the `bottom` row, then decrement `bottom`.
4. Check if `left < right`. If so, traverse from `bottom - 1` to `top - 1` along the `left` column, then increment `left`.

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        spiral = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        while top < bottom and left < right:

            # Traverse top row (left to right)
            for i in range(left, right):
                spiral.append(matrix[top][i])
            top += 1

            # Traverse right column (top to bottom)
            for i in range(top, bottom):
                spiral.append(matrix[i][right - 1])
            right -= 1

            # Traverse bottom row (right to left)
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    spiral.append(matrix[bottom - 1][i])
                bottom -=1

            # Traverse left column (bottom to top)
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    spiral.append(matrix[i][left])
                left += 1

        return spiral
```

### Dry Run Table
Input: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

*Initial Boundaries:* `top = 0`, `bottom = 3`, `left = 0`, `right = 3`

| Pass | Direction | Loop / Indices | Appended | New Boundary |
|---|---|---|---|---|
| **Iter 1** | Top Row | `(left, right) = (0, 3)` | `[1, 2, 3]` | `top = 1` |
| | Right Col | `(top, bottom) = (1, 3)` | `[6, 9]` | `right = 2` |
| | Bottom Row | `(right-1, left-1) = (1, -1)` *(valid: 1 < 3)* | `[8, 7]` | `bottom = 2` |
| | Left Col | `(bottom-1, top-1) = (1, 0)` *(valid: 0 < 2)* | `[4]` | `left = 1` |
| **Iter 2** | Top Row | `(left, right) = (1, 2)` | `[5]` | `top = 2` |
| | Right Col | `(top, bottom) = (2, 2)` | *None* | `right = 1` |
| | Bottom Row | *(invalid: top < bottom is False, 2 < 2)* | *None* | `bottom = 2` |
| | Left Col | *(invalid: left < right is False, 1 < 1)* | *None* | `left = 1` |

Loop terminates as `left < right` is now False ($1 < 1$). Result: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(M \times N)$ where $M$ is the number of rows and $N$ is the number of columns in the matrix. We visit every cell exactly once.
- **Space Complexity**: $O(1)$ auxiliary space as we only use boundary integers (`top`, `bottom`, `left`, `right`).

---

## 6. Mistakes & Lessons Learned

### Mistake #1: Incorrect Loop Termination Condition
- **Mistake**: Using division/round values based on original dimensions, e.g., `while top <= round(len(matrix)/2)...`
- **Correction**: Loop conditions should be dynamic, using direct comparison of running boundaries: `while top < bottom and left < right:`.

### Mistake #2: Missing Boundary Checks Before Reverse Traversals
- **Mistake**: Always executing the bottom-row and left-column traversals without verifying if the pointers crossed during the top/right passes in the same iteration. This causes duplicate element insertions in rectangular matrices.
- **Correction**: Wrap bottom-row traversal in `if top < bottom:` and left-column traversal in `if left < right:`.

### Key Takeaway Pattern
- Check conditions **immediately before** each directional traversal, not just at the start of the while loop.
- Test with rectangular matrices (not just squares) to ensure boundaries collapse correctly.
