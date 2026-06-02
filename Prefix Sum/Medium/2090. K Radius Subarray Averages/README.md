# 2090. K Radius Subarray Averages

**Difficulty:** Medium
**Link:** [LeetCode URL](https://leetcode.com/problems/k-radius-subarray-averages/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm uses a Prefix Sum array to precompute cumulative sums of the input array. This enables $O(1)$ computation of subarray sums for any fixed window of size $2k + 1$ centered around index $i$.

## 2. How to Recognize the Pattern

- **Subarray Sums/Averages of Fixed Size**: When you need to compute values (like averages or sums) for multiple contiguous subarrays of a fixed size, calculating the sum from scratch for each window results in $O(N \cdot K)$ complexity (brute force). 
- **Prefix Sum / Sliding Window**: Precomputing a prefix sum array or maintaining a sliding window sum reduces the time complexity to $O(N)$.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ — We make a single pass to build the prefix sum array ($O(N)$) and a second pass to compute the window averages ($O(N)$).
- **Space Complexity**: $O(N)$ — We store the prefix sums in a helper array of size $N$.

## 4. How It Works

1. Precompute the prefix sum of `nums` where `prefix_sum_array[i]` stores the sum of `nums[0...i]`.
2. Initialize `averages_array` with `-1` for all elements.
3. The valid range of center indices where a $2k + 1$ window can fit is from index $k$ to $nums\_len - k - 1$ (inclusive).
4. Iterate `i` through this valid range:
   - If `i == k`, the window starts at index `0`, so the sum is simply `prefix_sum_array[i + k]`.
   - Otherwise, the sum is `prefix_sum_array[i + k] - prefix_sum_array[i - k - 1]`.
5. Compute the average by performing integer division (`window_sum // (2 * k + 1)`), and assign it to `averages_array[i]`.
6. Return `averages_array`.

> [!IMPORTANT]
> **Implementation Note on Window Inclusivity**:
> When calculating the window sum for `i > k`, we subtract `prefix_sum_array[i - k - 1]`. Using `i - k - 1` is critical because it excludes all elements strictly before the window start (index `i - k`). Subtracting `i - k` instead would mistakenly drop the first element of our window, causing off-by-one average calculations.

```python
from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)

        # Pre-compute the prefix sum
        prefix_sum_array = [nums[0]]
        for i in range(1, nums_len):
            prefix_sum_array.append(prefix_sum_array[-1] + nums[i])

        # Calculate averages for entries where we
        # know for sure that there is a valid window
        averages_array = [-1] * nums_len
        window_size = 2 * k + 1
        for i in range(k, nums_len - k):
            if i == k: # This is for the very first entry of the window:
                window_sum = prefix_sum_array[i + k]
            else:
                # Note that we add a -1 to i - k - 1 because if we don't then the
                # window will be INCLUSIVE of the i-kth element, but we must drop
                # that so that you have the sum of all the previous values to the
                # i-kth value without including it so we don't mess up the average
                # calculations
                window_sum = prefix_sum_array[i + k] - prefix_sum_array[i - k - 1]
            averages_array[i] = window_sum // window_size
        return averages_array
```

### Dry Run Table
Input: `nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]`, `k = 3`  
`prefix_sum_array = [7, 11, 14, 23, 24, 32, 37, 39, 45]`  
`window_size = 7`

| Step/Index (`i`) | `i + k` | `i - k - 1` | Sum Calculation | `window_sum` | Average (`window_sum // 7`) | `averages_array` |
|------------------|---------|-------------|-----------------|--------------|-----------------------------|------------------|
| *init*           | —       | —           | —               | —            | —                           | `[-1, -1, -1, -1, -1, -1, -1, -1, -1]` |
| 3                | 6       | —           | `prefix[6]`     | 37           | 5                           | `[-1, -1, -1, 5, -1, -1, -1, -1, -1]` |
| 4                | 7       | 0           | `prefix[7] - prefix[0]` (39 - 7) | 32 | 4 | `[-1, -1, -1, 5, 4, -1, -1, -1, -1]` |
| 5                | 8       | 1           | `prefix[8] - prefix[1]` (45 - 11) | 34 | 4 | `[-1, -1, -1, 5, 4, 4, -1, -1, -1]` |
