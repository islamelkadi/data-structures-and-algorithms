# 977. Squares of a Sorted Array

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/squares-of-a-sorted-array/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Two Pointers (converging/opposite ends) technique. We compare the absolute values at the two ends of the sorted array and fill the result array from back to front.

## 2. How to Recognize the Pattern

- "sorted in non-decreasing order" + "return an array of the squares of each number sorted in non-decreasing order".
- Since the array is sorted, the largest squares must be at either the extreme left (negative numbers) or the extreme right (positive numbers).
- This indicates we should use two pointers starting at opposite ends and compare their absolute values to place the largest square at the end of the result array.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(N) where N is the length of `nums` because we only visit each element once using the two pointers.
- **Space Complexity**: O(N) or O(1) auxiliary space (excluding the output `result` array), as we only use a few pointer variables.
- A sorting approach squaring and sorting would take O(N log N) time, making this O(N) two-pointer solution optimal.

## 4. How It Works

1. Initialize `left` pointer to `0`, `right` pointer to `n - 1`, and `pos` pointer to `n - 1` (since we populate the largest squares first at the end of `result`).
2. Compare the absolute value of `nums[left]` and `nums[right]`:
   - If `abs(nums[right]) >= abs(nums[left])`, place the square of `nums[right]` at `result[pos]` and decrement `right`.
   - Otherwise, place the square of `nums[left]` at `result[pos]` and increment `left`.
3. Decrement `pos` at each step.
4. Continue until `pos < 0` and return the `result` array.

```python
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        pos = n - 1
        while pos >= 0:
            if abs(nums[right]) >= abs(nums[left]):
                result[pos] = nums[right] ** 2
                right -= 1
            else:
                result[pos] = nums[left] ** 2
                left += 1
            pos -= 1
        return result
```

### Dry Run Table
Input: `nums = [-4, -1, 0, 3, 10]`

`n = 5`, `result = [0, 0, 0, 0, 0]`

| Step | left | right | pos | nums[left] | nums[right] | Comparison: `abs(nums[right]) >= abs(nums[left])` | Action Taken | result |
|------|------|-------|-----|------------|-------------|---------------------------------------------------|--------------|--------|
| *init*| 0   | 4     | 4   | -4         | 10          | -                                                 | -            | `[0, 0, 0, 0, 0]` |
| 0    | 0    | 4     | 4   | -4         | 10          | `10 >= 4` → True                                  | `result[4] = 100`, `right -= 1` | `[0, 0, 0, 0, 100]` |
| 1    | 0    | 3     | 3   | -4         | 3           | `3 >= 4` → False                                  | `result[3] = 16`, `left += 1`   | `[0, 0, 0, 16, 100]` |
| 2    | 1    | 3     | 2   | -1         | 3           | `3 >= 1` → True                                   | `result[2] = 9`, `right -= 1`   | `[0, 0, 9, 16, 100]` |
| 3    | 1    | 2     | 1   | -1         | 0           | `0 >= 1` → False                                  | `result[1] = 1`, `left += 1`    | `[0, 1, 9, 16, 100]` |
| 4    | 2    | 2     | 0   | 0          | 0           | `0 >= 0` → True                                   | `result[0] = 0`, `right -= 1`   | `[0, 1, 9, 16, 100]` |

Result: `[0, 1, 9, 16, 100]`
