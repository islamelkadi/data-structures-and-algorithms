# 73. Set Matrix Zeroes

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/set-matrix-zeroes/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

In-place marking using the matrix's first row and first column as state flags, with separate tracking variables for the first row and first column themselves.

## 2. How to Recognize the Pattern

- **Set entire row/column to 0 based on cell values**: This requires keeping track of which rows and columns contain zeros.
- **Strict O(1) space constraint**: Since we cannot allocate an auxiliary row/column hash set or a copy of the matrix, we must store the flag indicators inside the input matrix itself.
- **First row/column as storage**: The first row and column are used as state stores, but because their own values will be overwritten, we must pre-record whether the first row and first column themselves initially contain any zeros.

## 3. Why This Algorithm Fits

- **$O(M \times N)$ time**: We perform two full traversals of the matrix.
- **$O(1)$ space**: Space is constant because we modify the input matrix in-place and only use two boolean variables (`first_row_zero` and `first_col_zero`).
- Avoiding marker pollution: Processing cells starting from index `(1,1)` in the second pass avoids interpreting recently zeroed markers as original zeros.

## 4. How It Works

1. Check if the first row contains any zero, and check if the first column contains any zero. Store these in booleans `first_row_zero` and `first_col_zero`.
2. Iterate through the rest of the matrix. If `matrix[row][col] == 0`, set the markers `matrix[row][0] = 0` and `matrix[0][col] = 0`.
3. Iterate from `row = 1` and `col = 1` upwards. If either `matrix[row][0] == 0` or `matrix[0][col] == 0`, set `matrix[row][col] = 0`.
4. Finally, if `first_row_zero` is True, zero out the entire first row. If `first_col_zero` is True, zero out the entire first column.

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        len_rows, len_cols = len(matrix), len(matrix[0])

        # Check if there are zeros in the first row
        first_row_zero = 0 in matrix[0]
        first_col_zero = any(matrix[r][0] == 0 for r in range(len_rows))

        # Pass 1: mark target rows / cols
        for row in range(len_rows):
            for col in range(len_cols):
                if matrix[row][col] == 0:
                    # To avoid a needless overwrite check if both
                    # the first row or col of that target are 0
                    # if yes continue, else overwrite
                    # if matrix[0][col] == 0 and matrix[row][0] == 0:
                    #     continue
                    
                    # A more concise (but less readable) way of the above
                    # commented out condition is as follows:
                    if (matrix[0][col] or matrix[row][0]) == 0:
                        continue
                    matrix[0][col] = matrix[row][0] = 0

        # BUG - you need to ignore the first
        # row and columns or you will accidentally
        # interpret recently zeroed out markers
        # as the new ground truth
        # Pass 2: set rows to zero
        for row in range(1, len_rows):
            for col in range(1, len_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            matrix[0][:] = [0] * len_cols

        if first_col_zero:
            for row in range(len_rows):
                matrix[row][0] = 0
```

### Dry Run Table
Input: `matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]`

- `first_row_zero = False`
- `first_col_zero = False`

**Pass 1 (Marking):**
- At `row = 1, col = 1`: `matrix[1][1] == 0` $\to$ set `matrix[0][1] = 0` and `matrix[1][0] = 0`.
- Matrix state after Pass 1: `[[1, 0, 1], [0, 0, 1], [1, 1, 1]]`.

**Pass 2 (Zeroing starting from (1, 1)):**

| row | col | matrix[row][0] == 0? | matrix[0][col] == 0? | Action | Matrix state |
|---|---|---|---|---|---|
| 1 | 1 | yes (0 == 0) | yes (0 == 0) | Set `matrix[1][1] = 0` | `[[1, 0, 1], [0, 0, 1], [1, 1, 1]]` |
| 1 | 2 | yes (0 == 0) | no (1 == 0) | Set `matrix[1][2] = 0` | `[[1, 0, 1], [0, 0, 0], [1, 1, 1]]` |
| 2 | 1 | no (1 == 0) | yes (0 == 0) | Set `matrix[2][1] = 0` | `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]` |
| 2 | 2 | no (1 == 0) | no (1 == 0) | *No change* | `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]` |

**First row/column adjustments:**
- `first_row_zero == False` $\to$ No change to row 0.
- `first_col_zero == False` $\to$ No change to col 0.

Result: `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(M \times N)$ where $M$ is the number of rows and $N$ is the number of columns. We iterate through all cells of the matrix a constant number of times.
- **Space Complexity**: $O(1)$ auxiliary space as we store markers in-place inside the first row and column of the matrix itself.
