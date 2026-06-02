# 724. Find Pivot Index

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/find-pivot-index/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Alternative Solution (Two Arrays)](#5-alternative-solution-two-arrays)

## 1. Algorithm Used

Prefix sum with derived suffix (single-pass). We maintain a running left sum and calculate the right sum on the fly.

## 2. How to Recognize the Pattern

- "Find an index where the sum of elements to the left equals the sum to the right" → pivot index → prefix sum + derived suffix.
- You need both a left aggregate and a right aggregate at each position → compute total once, derive the right side as `total - left_sum - nums[i]`.
- Brute force recomputes sums for every index (O(n²)); a single running total brings it to O(n).

## 3. Why This Algorithm Fits

- **Time Complexity**: O(n) — one pass to compute the total sum, and another pass to scan for the pivot.
- **Space Complexity**: O(1) — only a few variable registers, no additional arrays are needed.
- The right sum never needs to be stored or computed separately: `right_sum = total - prefix_sum - nums[i]`.

## 4. How It Works

Compute the total sum of the array. Walk left to right, maintaining a running `prefix_sum`. At each index `i`, check if `prefix_sum == total - prefix_sum - nums[i]`. If yes, this index is the pivot. If not, add `nums[i]` to `prefix_sum` and continue.

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = suffix_sum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            if prefix_sum == total - prefix_sum - nums[i]:
                return i
            prefix_sum += num
        return -1
```

Note that `suffix_sum` is initialized to `0` but is unused in the optimal single-pass version.

### Dry Run Table
Input: `nums = [1, 7, 3, 6, 5, 6]`, `total = 28`

| i | num | prefix_sum | right = `total - prefix_sum - num` | equal? | Action |
|---|-----|------------|------------------------------------|--------|--------|
| 0 | 1   | 0          | `28 - 0 - 1 = 27`                  | no     | `prefix_sum += 1` $\to$ 1 |
| 1 | 7   | 1          | `28 - 1 - 7 = 20`                  | no     | `prefix_sum += 7` $\to$ 8 |
| 2 | 3   | 8          | `28 - 8 - 3 = 17`                  | no     | `prefix_sum += 3` $\to$ 11 |
| 3 | 6   | 11         | `28 - 11 - 6 = 11`                 | yes    | Return `3` |

---

## 5. Alternative Solution (Two Arrays)

We can also precompute prefix and suffix sums using two separate arrays, then do a third pass to find the index where they match.

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        suffix_sum = [0] * len(nums)
        suffix_sum[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        for i in range(len(nums)):
            if prefix_sum[i] == suffix_sum[i]:
                return i
        return -1
```
- **Time Complexity**: O(n) (three sequential passes).
- **Space Complexity**: O(n) to store the prefix and suffix arrays.
