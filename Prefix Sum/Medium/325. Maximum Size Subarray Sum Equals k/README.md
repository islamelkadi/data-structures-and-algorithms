# 325. Maximum Size Subarray Sum Equals k

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Running prefix sum combined with a hashmap to find, in $O(N)$, the longest subarray whose elements sum to exactly $k$.

## 2. How to Recognize the Pattern

- **Subarray sum equals $k$**: Finding a contiguous subarray summing to $k$ suggests a prefix sum difference lookup: `prefix_sum - k`.
- **Maximum length**: Since we want to maximize the length of the subarray, we store the *first* occurrence of each prefix sum in the hash map.
- **Negative numbers / zeros**: Since the array can contain negative values and zeros, a sliding window is not applicable. Prefix sum + hashmap is the appropriate strategy.

## 3. Why This Algorithm Fits

- The algorithm performs a single pass over the array, achieving $O(N)$ time complexity.
- Storing the earliest index of each prefix sum allows us to compute the maximum possible distance `right - left` in $O(1)$ time whenever `prefix_sum - k` exists in our map.

## 4. How It Works

1. Maintain a running `prefix_sum` and a hash map `curr` initialized to `{0: -1}` to handle subarrays starting at index 0.
2. For each element at index `right`:
   - Add it to the running `prefix_sum`.
   - If this `prefix_sum` is not already in `curr`, record its first occurrence: `curr[prefix_sum] = right`.
   - Calculate the required complement `seen = prefix_sum - k`.
   - If `seen` exists in `curr`, update `ans` with the maximum length: `right - curr[seen]`.
3. Return `ans`.

```python
# We're trying to find the MAXIMUM LENGTH of a subarray
# When we find a prefix_sum - k in curr, we calculate length as: right - curr[seen]
# Setting curr[0] = -1 helps us handle the case where the subarray starts from index 0
# Example: if nums = [1,2,3] and k = 6, when we reach index 2, prefix_sum = 6
# We look for prefix_sum - k = 6 - 6 = 0
# Length = 2 - (-1) = 3, giving us the correct length for [1,2,3]

# THIS IS A LENGTH CALCUATION PROBLEM
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        # # Build prefix sum array
        # prefix_sum = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix_sum.append(nums[i] + prefix_sum[-1])
        
        # # Build prefix sum to index hashmap
        # curr = {0: -1}
        # for i, value in enumerate(prefix_sum):
        #     if value not in curr:
        #         curr[value] = i
        
        # # Get max len
        # ans = 0
        # for right in range(len(nums)):
        #     seen = prefix_sum[right] - k
        #     if seen in curr:
        #         ans = max(ans, right - curr[seen])
        # return ans

        prefix_sum = ans = 0
        curr = {0: -1}  # Initialize with 0 sum at index -1

        for right in range(len(nums)):
            prefix_sum += nums[right]
            if prefix_sum not in curr:
                curr[prefix_sum] = right
            seen = prefix_sum - k
            if seen in curr:
                ans = max(ans, right - curr[seen])
        return ans
```

### Dry Run Table
Input: `nums = [1, -1, 5, -2, 3]`, `k = 3`

| right | nums[right] | prefix_sum | in curr? | seen = ps-k | ans |
|-------|-------------|------------|----------|-------------|-----|
| *init*| —           | 0          | `{0: -1}` | —           | 0   |
| 0     | 1           | 1          | no $\to$ store `{1: 0}` | $1-3=-2$, not in curr | 0   |
| 1     | -1          | 0          | 0 in curr (`-1`) | $0-3=-3$, not in curr | 0   |
| 2     | 5           | 5          | no $\to$ store `{5: 2}` | $5-3=2$, not in curr | 0   |
| 3     | -2          | 3          | no $\to$ store `{3: 3}` | $3-3=0$, in curr (`-1`) $\to$ len = $3 - (-1) = 4$ | 4   |
| 4     | 3           | 6          | no $\to$ store `{6: 4}` | $6-3=3$, in curr (`3`) $\to$ len = $4 - 3 = 1$ | 4   |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. We iterate through the array once and perform $O(1)$ lookup operations.
- **Space Complexity**: $O(N)$ auxiliary space as the hash map `curr` can store up to $N$ unique prefix sums in the worst case.
