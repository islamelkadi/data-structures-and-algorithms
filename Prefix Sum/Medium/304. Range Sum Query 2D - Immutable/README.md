## 1. Algorithm Used

2D prefix sum built in two passes (row-wise then column-wise), with 0-padding for clean range queries.

## 2. How to Recognize the Pattern

- "Multiple submatrix sum queries on an immutable matrix" → precompute prefix sums once, answer each query in O(1).
- 2D range query → extend 1D prefix sum to two dimensions.

## 3. Why This Algorithm Fits

- O(m*n) preprocessing, O(1) per query.
- Two separate 1D passes (row then column) are easier to reason about than a single combined formula.
- 0-padding on the left and top eliminates boundary checks in `sumRegion`.

## 4. How It Works

Pass 1 — row prefix: for each row, accumulate left to right so `matrix[r][c]` holds the sum of the original row from column 0 to c.

Pass 2 — column prefix: for each column, accumulate top to bottom so `matrix[r][c]` now holds the sum of the entire submatrix from `(0,0)` to `(r,c)`.

Then prepend a zero column on the left and a zero row on top. This shifts all indices by 1, so `sumRegion` can subtract without worrying about index -1.

```python
top_range_prefix = self.matrix[row1][col2] - self.matrix[row1][col1]
bottom_range_prefix = self.matrix[row2][col2] - self.matrix[row2][col1]
return bottom_range_prefix - top_range_prefix
```

`bottom_range_prefix` is the sum of the full submatrix up to `(row2, col2)` minus the columns left of `col1`. Subtracting `top_range_prefix` removes the rows above `row1`.

Input matrix:
```
3  0  1  4  2
5  6  3  2  1
1  2  0  1  5
4  1  0  1  7
1  0  3  0  5
```

After Pass 1 (row prefix — each cell = sum of row from col 0 to col c):
```
3   3   4   8  10
5  11  14  16  17
1   3   3   4   9
4   5   5   6  13
1   1   4   4   9
```

After Pass 2 (column prefix — each cell += cell from row above):
```
 3   3   4   8  10
 8  14  18  24  27
 9  17  21  28  36
13  22  26  34  49
14  23  30  38  58
```

After padding (prepend zero column left, zero row top):
```
 0   0   0   0   0   0
 0   3   3   4   8  10
 0   8  14  18  24  27
 0   9  17  21  28  36
 0  13  22  26  34  49
 0  14  23  30  38  58
```

Query `sumRegion(2, 1, 4, 3)` (rows 2-4, cols 1-3):
- col2+1=4, row2+1=5
- top = matrix[2][4] - matrix[2][1] = 24 - 8 = 16
- bottom = matrix[5][4] - matrix[5][1] = 38 - 14 = 24
- result = 24 - 16 = 8 ✓ (2+0+1+1+0+1+0+3+0 = 8)

## 5. When to Use Padding vs Not

The need for padding comes down to whether you're doing range queries or just point lookups.

**No padding needed** — if you only need the prefix value at a single point (sum from `(0,0)` to `(r,c)`), you can index directly into the prefix matrix without any risk of going out of bounds.

**Padding is needed** — when you need arbitrary range queries like `sumRegion(row1, col1, row2, col2)`, you subtract prefix values. Without padding, querying a range that starts at row 0 or column 0 would require `row1 - 1 = -1` or `col1 - 1 = -1`, causing an index error.

The 0-padding acts as a sentinel: `prefix[0][...] = 0` and `prefix[...][0] = 0`, so subtracting them is always safe and always correct.

Without padding you'd need explicit guards:
```python
# messy — special case every time col1 or row1 is 0
left = prefix[row][col1 - 1] if col1 > 0 else 0
```

With padding that goes away entirely — every query uses the same formula with no conditionals.

The same logic applies in 1D: padding with a leading 0 lets you write `prefix[r+1] - prefix[l]` for any `l`, including `l = 0`, without a special case.

## 6. Time & Space Complexity

Time: O(m*n) to build, O(1) per query.

Space: O(m*n) — the matrix is modified in-place (plus one extra row and column for padding).
