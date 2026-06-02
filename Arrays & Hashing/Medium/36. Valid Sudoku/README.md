# 36. Valid Sudoku

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/valid-sudoku/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Three-set validation — maintain one `defaultdict(set)` each for rows, columns, and 3×3 boxes, and check each digit against all three before inserting it.

## 2. How to Recognize the Pattern

- **Validate grid constraints (no repeats)**: We must ensure no duplicate digits exist within any row, column, or sub-grid, suggesting we use sets to track seen elements.
- **Sub-grid mapping**: The 3×3 box index for any cell at `(row, col)` can be computed using `(row // 3, col // 3)`.

## 3. Why This Algorithm Fits

- **$O(1)$ time**: The board is always $9 \times 9$, meaning we evaluate at most 81 cells.
- **$O(1)$ space**: The sets collectively store at most 81 entries.
- A single pass over the board is sufficient; no backtracking or sorting is needed.

## 4. How It Works

Iterate over every cell. Skip cells containing `"."`. For each digit, check whether it already appears in the current row's set, the current column's set, or the current box's set (keyed by `(row // 3, col // 3)`). If any check fails, return `False`. Otherwise, add the digit to all three sets and continue.

```python
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        array_length = 9
        grid_length = 3
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        grid_seen = defaultdict(set)

        for row in range(array_length):
            for col in range(array_length):

                if board[row][col] == ".":
                    continue

                if board[row][col] in row_seen[row] or board[row][col] in col_seen[col] or board[row][col] in grid_seen[(row // grid_length, col // grid_length)]:
                    return False
                
                # Add to row
                row_seen[row].add(board[row][col])

                # Add to col
                col_seen[col].add(board[row][col])

                # Add to grid
                grid_seen[(row // grid_length, col // grid_length)].add(board[row][col])
        
        return True
```

The `(row // 3, col // 3)` key is the key insight: integer division maps all nine cells of a 3×3 box to the same tuple, so no explicit box-boundary arithmetic is needed.

### Dry Run Table (Partial)
Input board has `5` at (0,0), `3` at (0,1), `7` at (0,4)

| row | col | val | row_seen[0] | col_seen | grid_seen[(0,0)] | valid? |
|---|---|---|---|---|---|---|
| 0 | 0 | 5 | `{}` | `{}` | `{}` | add all |
| 0 | 1 | 3 | `{5}` | `{3}` | `{5}` | add all |
| 0 | 4 | 7 | `{5, 3}` | `{7}` | `{5, 3}` | add all |
| 0 | 0 | 5 (dup) | `{5, 3, 7}` | — | — | 5 in `row_seen[0]` $\to$ `False` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(1)$ because the grid size is fixed at $9 \times 9$, restricting the iterations to a constant of 81. For an $N \times N$ board, the time complexity would be $O(N^2)$.
- **Space Complexity**: $O(1)$ auxiliary space because the maximum memory allocation is bounded by the 81 cell values. For an $N \times N$ board, the space complexity would be $O(N^2)$.
