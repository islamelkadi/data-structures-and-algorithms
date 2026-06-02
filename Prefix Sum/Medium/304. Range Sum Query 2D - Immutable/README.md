# 304. Range Sum Query 2D - Immutable

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/range-sum-query-2d-immutable/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. When to Use Padding vs Not](#5-when-to-use-padding-vs-not)
6. [6. Time & Space Complexity](#6-time--space-complexity)

## 1. Algorithm Used

2D prefix sum built in two passes (row-wise then column-wise), with 0-padding for clean range queries.

## 2. How to Recognize the Pattern

- **Multiple submatrix sum queries on an immutable matrix**: Precomputing prefix sums once allows us to answer each query in $O(1)$ time.
- **2D range query**: Extending 1D prefix sum to two dimensions.

## 3. Why This Algorithm Fits

- $O(M \times N)$ preprocessing time, and $O(1)$ per query.
- Two separate 1D passes (row-wise then column-wise) are easier to reason about than a single combined formula.
- 0-padding on the left and top eliminates boundary checks in `sumRegion`.

## 4. How It Works

1. **Pass 1 — Row prefix**: Accumulate row values from left to right. `matrix[r][c]` holds the sum of row `r` from column 0 to `c`.
2. **Pass 2 — Column prefix**: Accumulate column values from top to bottom. `matrix[r][c]` now holds the sum of the entire submatrix from `(0,0)` to `(r,c)`.
3. Prepend a zero column on the left and a zero row on top. This shifts all indices by 1, so `sumRegion` can subtract without worrying about index -1.
4. **Range Query calculation**:
   - `bottom_range_prefix` represents the sum of elements in columns `col1` to `col2`, from row 0 to `row2`.
   - `top_range_prefix` represents the sum of elements in columns `col1` to `col2`, from row 0 to `row1 - 1`.
   - Subtracting `top_range_prefix` from `bottom_range_prefix` yields the sum of the region from `row1` to `row2` and `col1` to `col2`.

```python
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

        # Create row based prefix (left to right)
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(1, cols):
                # Where row, col - 1 means same row but the column
                # before it
                matrix[row][col] += matrix[row][col - 1]

        # Create col based prefix (top to bottom)
        for row in range(1, rows):
            for col in range(cols):
                # Where row - 1, col means the same PRIOR row at each
                # new columns
                matrix[row][col] +=  matrix[row - 1][col]

        # Insert left padding
        for row in range(rows):
            matrix[row] = [0] + matrix[row]
        
        # Insert top padding
        # Re-compute number of columns because of added padding,
        # which means an extra column
        cols = len(matrix[0])
        self.matrix = [[0] * cols] + self.matrix

    # def prefixSum(self, array):
    #     prefix = [array[0]]
    #     for i in range(1, len(array)):
    #         prefix.append(array[i] + prefix[-1])
    #     return prefix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        col2 += 1 # Incrementing col2 due to left based padding
        row2 += 1 # Incrementing row2 due to left based padding

        top_range_prefix = self.matrix[row1][col2] - self.matrix[row1][col1]
        bottom_range_prefix = self.matrix[row2][col2] - self.matrix[row2][col1]
        
        return bottom_range_prefix - top_range_prefix
```

### Dry Run Example
Input Matrix:
```
3  0  1  4  2
5  6  3  2  1
1  2  0  1  5
4  1  0  1  7
1  0  3  0  5
```

After Pass 1 (Row Prefix):
```
3   3   4   8  10
5  11  14  16  17
1   3   3   4   9
4   5   5   6  13
1   1   4   4   9
```

After Pass 2 (Column Prefix):
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

Query `sumRegion(row1=2, col1=1, row2=4, col2=3)` (rows 2-4, cols 1-3):
- Shifted values: `row1 = 2`, `col1 = 1`, `row2 = 4 + 1 = 5`, `col2 = 3 + 1 = 4`.
- `bottom_range_prefix` = `matrix[5][4] - matrix[5][1]` = `38 - 14 = 24`.
  *(Sum of columns 1 to 3, from row 0 to row 4)*
- `top_range_prefix` = `matrix[2][4] - matrix[2][1]` = `24 - 8 = 16`.
  *(Sum of columns 1 to 3, from row 0 to row 1)*
- **Final Result** = `bottom_range_prefix - top_range_prefix` = `24 - 16 = 8`.

---

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

---

## 6. Time & Space Complexity

- **Time Complexity**: 
  - **Constructor**: $O(M \times N)$ to iterate and build the prefix sums.
  - **sumRegion**: $O(1)$ constant time lookup and subtraction.
- **Space Complexity**: $O(M \times N)$ space for storing the prefix sum matrix.
