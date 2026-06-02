# 303. Range Sum Query - Immutable

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/range-sum-query-immutable/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Precompute a prefix sum array so that any range sum query can be answered in $O(1)$ using `prefix[right] - prefix[left-1]`.

## 2. How to Recognize the Pattern

- **Multiple range sum queries**: Repeated range sum queries on an immutable array point to prefix sum precomputation.
- **Sum of a contiguous subarray**: Finding the sum of elements from index `left` to `right` is computed as `prefix[right] - prefix[left - 1]`.

## 3. Why This Algorithm Fits

- The constructor builds the prefix sum array in $O(N)$ time.
- Queries are resolved in $O(1)$ time by performing a subtraction of two precomputed values, which is optimal for multiple query calls.

## 4. How It Works

During initialization, build a prefix sum array `self._prefix_sum` where each index `i` stores the sum of all elements from index 0 to `i`.
For a query `sumRange(left, right)`:
- If `left == 0`, return `prefix[right]`.
- Otherwise, return `prefix[right] - prefix[left - 1]`. The subtraction removes the sum of the elements before index `left`.

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self._prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self._prefix_sum.append(nums[i] + self._prefix_sum[-1])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum[right]
        # The left - 1 is because you do not want to include left
        # this is because you would essentially subtracting the
        # prefix sum with the left pointer being considered, when
        # it should be up until the left pointer but not including
        # it.
        return self._prefix_sum[right] - self._prefix_sum[left - 1]
```

### Dry Run Example
Input: `nums = [-2, 0, 3, -5, 2, -1]`

Prefix Array (`self._prefix_sum`):
```
[-2, -2, 1, -4, -6, -7]
```

| i   | nums[i] | prefix[i] |
|-----|---------|-----------|
| 0   | -2      | -2        |
| 1   | 0       | -2        |
| 2   | 3       | 1         |
| 3   | -5      | -4        |
| 4   | 2       | -2        |
| 5   | -1      | -3        |

- Query `sumRange(0, 2)` $\to$ `left == 0` $\to$ returns `prefix[2] = 1`.
- Query `sumRange(2, 5)` $\to$ returns `prefix[5] - prefix[1] = -3 - (-2) = -1`.

---

## 5. Time & Space Complexity

- **Time Complexity**:
  - **Constructor**: $O(N)$ where $N$ is the number of elements in `nums`. We traverse the array once to build the prefix sums.
  - **sumRange**: $O(1)$ constant time lookup and subtraction.
- **Space Complexity**: $O(N)$ auxiliary space to store the prefix sum array.
