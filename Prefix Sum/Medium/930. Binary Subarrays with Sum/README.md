# 930. Binary Subarrays with Sum

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/binary-subarrays-with-sum/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Alternative Solution (Prefix Sum + HashMap)](#5-alternative-solution-prefix-sum--hashmap)

## 1. Algorithm Used

At-Most-Sum Sliding Window Trick. We calculate the count of subarrays with sum at most `goal` and subtract the count of subarrays with sum at most `goal - 1`. This isolates the subarrays with sum exactly equal to `goal`.

## 2. How to Recognize the Pattern

- "find the number of non-empty subarrays with a sum equal to goal" where the array elements are only `0` and `1` (binary array).
- Since elements are non-negative, the prefix sum is monotonic, allowing a sliding window approach.
- Direct sliding window for an *exact* sum is difficult to count because of trailing zeros. Applying the "At-Most" subtraction trick (`exactly(goal) = at_most(goal) - at_most(goal - 1)`) simplifies it.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(N) because the sliding window helper function is called twice, and each call scans the array in linear time.
- **Space Complexity**: O(1) auxiliary space, which is an improvement over the O(N) space required by the HashMap prefix sum approach.

## 4. How It Works

`numSubarraysWithAtmostSum(nums, goal)` counts all subarrays with sum ≤ `goal`.
1. Expand the `right` pointer and add `nums[right]` to `curr` (the running sum).
2. While `curr > goal` and `left <= right`, increment the `left` pointer and subtract `nums[left]` from `curr`.
3. Add `right - left + 1` to `ans` (the number of valid subarrays ending at `right`).
4. Subtract `numSubarraysWithAtmostSum(nums, goal - 1)` from `numSubarraysWithAtmostSum(nums, goal)` to get the final count.

```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def numSubarraysWithAtmostSum(nums, goal):
            left = curr = ans = 0
            for right in range(len(nums)):
                curr += nums[right]
                while curr > goal and left <= right:
                    curr -= nums[left]
                    left += 1
                ans += right - left + 1
            return ans
        return numSubarraysWithAtmostSum(nums, goal) - numSubarraysWithAtmostSum(nums, goal - 1)
```

### Dry Run Table
Input: `nums = [1, 0, 1, 0, 1]`, `goal = 2`

**`numSubarraysWithAtmostSum(nums, 2)`:**

| right | nums[right] | curr (sum) | left | Window size (valid) | ans (added) |
|-------|-------------|------------|------|---------------------|-------------|
| 0     | 1           | 1          | 0    | 1                   | 1           |
| 1     | 0           | 1          | 0    | 2                   | 3           |
| 2     | 1           | 2          | 0    | 3                   | 6           |
| 3     | 0           | 2          | 0    | 4                   | 10          |
| 4     | 1           | 3 > 2 → shrink to left=1 | 1 | 4 (`[0, 1, 0, 1]`) | 14 |

**`numSubarraysWithAtmostSum(nums, 1)`:**

| right | nums[right] | curr (sum) | left | Window size (valid) | ans (added) |
|-------|-------------|------------|------|---------------------|-------------|
| 0     | 1           | 1          | 0    | 1                   | 1           |
| 1     | 0           | 1          | 0    | 2                   | 3           |
| 2     | 1           | 2 > 1 → shrink to left=2 | 2 | 1 (`[1]`) | 4           |
| 3     | 0           | 1          | 2    | 2                   | 6           |
| 4     | 1           | 2 > 1 → shrink to left=4 | 4 | 1 (`[1]`) | 7           |

Result = `14 - 7 = 7`

---

## 5. Alternative Solution (Prefix Sum + HashMap)

We can also use a prefix sum with a frequency hashmap. This is more generalizable as it works for arrays with negative numbers (where sliding window does not apply).

```python
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        curr_sum = count = 0
        for num in nums:
            curr_sum += num
            count += prefix_count[curr_sum - goal]
            prefix_count[curr_sum] += 1
        return count
```
- **Time Complexity**: O(N)
- **Space Complexity**: O(N) to store the prefix frequencies in the hashmap.
