# 48. Rotate Image

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/rotate-image/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

In-place matrix transposition followed by row reversal.

## 2. How to Recognize the Pattern

- **Rotate a 2D matrix by 90 degrees clockwise in-place**: This is a classic grid transformation. Instead of using complex cell-coordinate math, a clockwise rotation is mathematically equivalent to transposing the matrix first, then reversing each row.
- **Strict in-place requirements**: Forces swapping elements directly inside the input matrix rather than copying cells to a new output grid.

## 3. Why This Algorithm Fits

- **$O(N^2)$ time**: Requires visiting each cell in the $N \times N$ matrix a constant number of times.
- **$O(1)$ space**: Runs entirely in-place. Swapping `matrix[i][j]` with `matrix[j][i]` and reversing rows is done directly on the input matrix, avoiding auxiliary memory allocation.

## 4. How It Works

1. **Transpose the matrix**: Iterate through the upper triangle of the matrix (where `col > row`) and swap `matrix[i][j]` with `matrix[j][i]`. This reflects the elements along the main diagonal.
2. **Reverse each row**: Traverse each row of the transposed matrix and reverse its elements in-place. This shifts columns from the outer edges inward.

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
```

### Dry Run Table
Input: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

**Step 1: Transposition (reflect along diagonal)**

| i | j | matrix[i][j] | matrix[j][i] | Action (Swap) | Resulting Matrix |
|---|---|---|---|---|---|
| 0 | 1 | 2 | 4 | Swap `matrix[0][1]` and `matrix[1][0]` | `[[1, 4, 3], [2, 5, 6], [7, 8, 9]]` |
| 0 | 2 | 3 | 7 | Swap `matrix[0][2]` and `matrix[2][0]` | `[[1, 4, 7], [2, 5, 6], [3, 8, 9]]` |
| 1 | 2 | 6 | 8 | Swap `matrix[1][2]` and `matrix[2][1]` | `[[1, 4, 7], [2, 5, 8], [3, 6, 9]]` |

**Step 2: Row Reversal**

| i | Transposed Row | Reversed Result |
|---|---|---|
| 0 | `[1, 4, 7]` | `[7, 4, 1]` |
| 1 | `[2, 5, 8]` | `[8, 5, 2]` |
| 2 | `[3, 6, 9]` | `[9, 6, 3]` |

Result: `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N^2)$ where $N$ is the number of rows/columns in the matrix. Transposing takes $\frac{N(N-1)}{2}$ swaps, and reversing $N$ rows takes $N \times \frac{N}{2}$ swaps, both of which are proportional to the number of cells in the grid.
- **Space Complexity**: $O(1)$ auxiliary space as the entire transformation is done in-place.
