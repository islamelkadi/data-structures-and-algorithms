# 2352. Equal Row and Column Pairs
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/equal-row-and-column-pairs/

## 1. Algorithm Used

Tuple hashing — count row tuples, then compare each column tuple against the row count map.

## 2. How to Recognize the Pattern

- "count matching row-column pairs in a grid" → convert rows and columns to tuples → use a Counter for O(1) lookup.
- Tuples are hashable in Python, making them ideal keys for frequency maps.

## 3. Why This Algorithm Fits

- O(n²) time — building row tuples is O(n²), building each column tuple is O(n), done n times.
- O(n²) space — storing all row tuples in the counter.
- Counter lookup is O(1), so comparing all n columns is O(n²) total.

## 4. How It Works

Build a Counter of all row tuples. For each column index, construct the column tuple by reading down that column. Add the count of matching rows to the result.

```python
from typing import List
from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counts = Counter(tuple(row) for row in grid)
        count = 0
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            count += row_counts[col_tuple]
        return count
```

`row_counts[col_tuple]` returns 0 if the column tuple has no matching row, so no special-casing is needed — the Counter handles missing keys gracefully.

Input: `grid = [[3,2,1],[1,7,6],[2,7,7]]`

| step | row tuples | col tuples | matches |
|------|------------|------------|---------|
| rows | (3,2,1):1, (1,7,6):1, (2,7,7):1 | | |
| col 0 | | (3,1,2) | 0 |
| col 1 | | (2,7,7) | (2,7,7) in rows → 1 |
| col 2 | | (1,6,7) | 0 |
| result | | | 1 |
