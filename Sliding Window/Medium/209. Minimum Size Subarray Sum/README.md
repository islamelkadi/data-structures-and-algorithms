# 209. Minimum Size Subarray Sum

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/minimum-size-subarray-sum/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Variable sliding window that shrinks from the left whenever the running sum meets or exceeds `target`, minimizing the window length at each valid state.

## 2. How to Recognize the Pattern

- **Minimum length subarray with sum $\ge$ target**: Finding a contiguous subarray with a sum threshold points to a shrink-when-valid sliding window.
- **Positive elements**: Since all numbers are positive, expanding the window (`right` pointer) strictly increases the sum and contracting the window (`left` pointer) strictly decreases the sum. This monotonic property guarantees that the sliding window is correct.
- **Minimize length (not maximize)**: Because we want to minimize the length, we record the minimum window size inside the shrink loop (while the window is valid), rather than at the end of the expansion step.

## 3. Why This Algorithm Fits

- The two pointers `left` and `right` traverse the array in a single direction, leading to $O(N)$ time complexity.
- Maintaining only three scalar variables (`left`, `curr`, and `ans`) satisfies the $O(1)$ space requirement.

## 4. How It Works

1. Initialize `left = 0`, `curr = 0`, and `ans = float("inf")`.
2. Expand the window by advancing `right` and adding `nums[right]` to the running sum `curr`.
3. While the window sum is valid (`curr >= target`):
   - Update the minimum length: `ans = min(ans, right - left + 1)`.
   - Shrink the window by subtracting `nums[left]` from `curr` and incrementing `left`.
4. Return 0 if `ans` remains infinity (meaning no valid subarray was found), otherwise return `ans`.

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0
        ans = float("inf")
        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1
        return 0 if ans == float("inf") else ans
```

### Dry Run Table
Input: `nums = [2, 3, 1, 2, 4, 3]`, `target = 7`

| right | nums[right] | curr | curr $\ge$ 7? | left | ans |
|---|---|---|---|---|---|
| 0 | 2 | 2 | no | 0 | inf |
| 1 | 3 | 5 | no | 0 | inf |
| 2 | 1 | 6 | no | 0 | inf |
| 3 | 2 | 8 | yes $\to$ `ans = 4`, shrink | 1 (`curr = 6`) | 4 |
| 4 | 4 | 10 | yes $\to$ `ans = 4`, shrink | 2 (`curr = 7`) $\to$ `ans = 3`, shrink | 3 (`curr = 6`) | 3 |
| 5 | 3 | 9 | yes $\to$ `ans = 3`, shrink | 4 (`curr = 7`) $\to$ `ans = 2`, shrink | 5 (`curr = 3`) | 2 |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of `nums`. Each element is visited at most twice: once by the `right` pointer and at most once by the `left` pointer.
- **Space Complexity**: $O(1)$ auxiliary space as we only use a few scalar trackers.
