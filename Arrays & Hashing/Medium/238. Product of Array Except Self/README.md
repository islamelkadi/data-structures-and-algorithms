# 238. Product of Array Except Self

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/product-of-array-except-self/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Prefix and Suffix product arrays (running products from both directions).

## 2. How to Recognize the Pattern

- **"Product of all elements except self" without using division**: Since division is forbidden, we cannot simply find the total product and divide by `nums[i]`. We must find the product of everything to the left of `i` and multiply it by the product of everything to the right of `i`.
- **Contiguous subsegment products**: The elements to the left form a prefix, and the elements to the right form a suffix. Precomputing these aggregates is a classic Prefix/Suffix Sum pattern.

## 3. Why This Algorithm Fits

- The prefix array stores the product of elements from index 0 up to `i`.
- The suffix array stores the product of elements from index `i` down to the end.
- Using these two precomputed structures, we can compute the product of all elements except `nums[i]` in $O(1)$ time by multiplying `prefix[i - 1] * suffix[i + 1]`.

## 4. How It Works

1. Initialize `prefix` with the first element: `prefix = [nums[0]]`. Iterate left-to-right to accumulate products: `prefix.append(nums[i] * prefix[-1])`.
2. Initialize `suffix` of size $N$ with 1s. Set `suffix[-1] = nums[-1]`. Iterate right-to-left to accumulate products: `suffix[i] = nums[i] * suffix[i+1]`.
3. Loop through each index `i` from 0 to $N - 1$:
   - For `i == 0`, the product is `1 * suffix[i + 1]`.
   - For `i == n - 1`, the product is `prefix[i - 1] * 1`.
   - Otherwise, the product is `prefix[i - 1] * suffix[i + 1]`.
4. Overwrite `nums[i]` with the calculated product and return `nums`.

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Prefix array
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] * prefix[-1])

        # Suffix array
        suffix = [1] * n
        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]

        # Return products
        for i in range(n):
            if i == 0:
                nums[i] = 1 * suffix[i + 1]
            elif i == n - 1:
                nums[i] = prefix[i - 1] * 1
            else:
                nums[i] = prefix[i - 1] * suffix[i + 1]
        return nums
```

### Dry Run Example
Input: `nums = [1, 2, 3, 4]`

#### 1. Prefix Products Generation
- `prefix[0] = 1`
- `prefix[1] = 2 * 1 = 2`
- `prefix[2] = 3 * 2 = 6`
- `prefix[3] = 4 * 6 = 24`
- `prefix` array state: `[1, 2, 6, 24]`

#### 2. Suffix Products Generation
- `suffix[3] = 4`
- `suffix[2] = 3 * 4 = 12`
- `suffix[1] = 2 * 12 = 24`
- `suffix[0] = 1 * 24 = 24`
- `suffix` array state: `[24, 24, 12, 4]`

#### 3. Product Construction Table

| i | prefix[i - 1] | suffix[i + 1] | Calculation | nums[i] (result) |
|---|---|---|---|---|
| 0 | — | `suffix[1] = 24` | `1 * 24` | 24 |
| 1 | `prefix[0] = 1` | `suffix[2] = 12` | `1 * 12` | 12 |
| 2 | `prefix[1] = 2` | `suffix[3] = 4` | `2 * 4` | 8 |
| 3 | `prefix[2] = 6` | — | `6 * 1` | 6 |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. We perform three linear passes (prefix pass, suffix pass, and result reconstruction).
- **Space Complexity**: $O(N)$ auxiliary space to store the `prefix` and `suffix` arrays of size $N$.
  - *Note*: An $O(1)$ auxiliary space optimization is possible by using the output array to accumulate prefix products and multiplying suffix products using a running scalar variable.
