# 36. Valid Sudoku
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/valid-sudoku/

## 1. Algorithm Used

Three-set validation: maintain one `defaultdict(set)` each for rows, columns, and 3×3 boxes, and check each digit against all three before inserting it.

## 2. How to Recognize the Pattern

- "no digit may repeat in a row, column, or sub-grid" → track seen values per group → one set per group.
- Three independent constraints must all hold simultaneously → three separate data structures.
- The 3×3 box a cell belongs to is determined by `(row // 3, col // 3)` → use that tuple as the key.

## 3. Why This Algorithm Fits

- O(1) time — the board is always 9×9, so the total work is bounded by 81 cells.
- O(1) space — the sets collectively hold at most 81 entries.
- A single pass over the board is sufficient; no backtracking or sorting needed.

## 4. How It Works

Iterate over every cell. Skip cells containing `"."`. For each digit, check whether it already appears in the current row's set, the current column's set, or the current box's set (keyed by `(row // 3, col // 3)`). If any check fails, return False. Otherwise add the digit to all three sets and continue.

```python
row_seen = defaultdict(set)
col_seen = defaultdict(set)
grid_seen = defaultdict(set)

for row in range(9):
    for col in range(9):
        val = board[row][col]
        if val == ".":
            continue
        if val in row_seen[row] or val in col_seen[col] or val in grid_seen[(row // 3, col // 3)]:
            return False
        row_seen[row].add(val)
        col_seen[col].add(val)
        grid_seen[(row // 3, col // 3)].add(val)
return True
```

The `(row // 3, col // 3)` key is the key insight: integer division maps all nine cells of a 3×3 box to the same tuple, so no explicit box-boundary arithmetic is needed.
