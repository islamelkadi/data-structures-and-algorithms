# 2643. Row With Maximum Ones

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/row-with-maximum-ones/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm performs a single pass over the matrix rows. It computes the sum of elements for each row (which equals the number of `1`s since the matrix is binary) and updates the tracker for the row index and maximum frequency of `1`s whenever a row contains strictly more `1`s than the maximum found so far.

## 2. How to Recognize the Pattern

- **Matrix Traversal**: We are asked to find the row with the maximum number of `1`s. Since the matrix needs to be fully inspected, iterating row-by-row and summing the row elements is the most direct solution.
- **Tie-Breaking Rule**: The problem states: *"If there are multiple rows that have the maximum number of ones, return the row with the smallest row number."* By updating our maximum only when the current row's count is **strictly greater** than the best so far (`total_sum > final_ans`), we naturally preserve the smallest index.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(M \times N)$ where $M$ is the number of rows and $N$ is the number of columns. We visit every cell in the matrix once to calculate the row sums.
- **Space Complexity**: $O(1)$ auxiliary space, as we only maintain two integer variables (`row_index` and `final_ans`) to track the result.

## 4. How It Works

1. Initialize `row_index = 0` and `final_ans = 0`.
2. Iterate through each row in the matrix using its index `i` (via `enumerate`).
3. Calculate the sum of the row.
4. If the row sum is strictly greater than `final_ans`, update `row_index = i` and `final_ans = sum`.
5. Return `[row_index, final_ans]`.

```python
from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row_index = 0
        final_ans = 0
        for i, row in enumerate(mat):
            total_sum = sum(row)
            if total_sum > final_ans:
                row_index = i
                final_ans = total_sum
        return [row_index, final_ans]
```

### Dry Run Table
Input: `mat = [[0, 1], [1, 0], [1, 1]]`

| Step/Index | `row` | `total_sum` | Condition (`total_sum > final_ans`) | `row_index` | `final_ans` | Action Taken |
|------------|-------|-------------|-----------------------------------|-------------|-------------|--------------|
| *init*     | —     | —           | —                                 | 0           | 0           | Initialize tracking variables |
| 0          | `[0, 1]`| 1         | `1 > 0` (True)                    | 0           | 1           | Update `row_index` and `final_ans` |
| 1          | `[1, 0]`| 1         | `1 > 1` (False)                   | 0           | 1           | Skip (retains smaller index `0` on tie) |
| 2          | `[1, 1]`| 2         | `2 > 1` (True)                    | 2           | 2           | Update `row_index` and `final_ans` |
