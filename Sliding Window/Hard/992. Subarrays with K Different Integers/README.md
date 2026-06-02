# 992. Subarrays with K Different Integers
**Difficulty:** Hard
**Link:** https://leetcode.com/problems/subarrays-with-k-different-integers/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used
at-most-k trick: answer = atMost(k) - atMost(k-1), where atMost counts subarrays with at most k distinct integers.

## 2. How to Recognize the Pattern
- "exactly k distinct" → direct sliding window is hard because the window can't stay "exactly k" cleanly → reframe as atMost(k) - atMost(k-1).
- Whenever a problem asks for "exactly k" of something countable, consider the at-most subtraction trick.

## 3. Why This Algorithm Fits
- O(n) time — two linear passes (atMost called twice).
- O(k) space — frequency map holds at most k+1 distinct keys before shrinking.
- atMost(k) is easy to implement with a standard variable window; the subtraction isolates the "exactly k" case.

## 4. How It Works

`subarraysWithAtmostKDistinct(nums, k)` counts all subarrays with ≤ k distinct integers using a frequency map. When `len(curr) > k`, shrink from the left, deleting entries that reach zero frequency. Each valid right position contributes `right - left + 1` subarrays. Subtracting `subarraysWithAtmostKDistinct(nums, k-1)` from `subarraysWithAtmostKDistinct(nums, k)` leaves only subarrays with exactly k distinct integers.

```python
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithAtmostKDistinct(nums, k):
            curr = {}
            left = ans = 0
            for right in range(len(nums)):
                curr[nums[right]] = curr.get(nums[right], 0) + 1
                while len(curr) > k and left <= right:
                    curr[nums[left]] -= 1
                    if curr[nums[left]] == 0:
                        del curr[nums[left]]
                    left += 1
                ans += right - left + 1
            return ans
        return subarraysWithAtmostKDistinct(nums, k) - subarraysWithAtmostKDistinct(nums, k - 1)
```

The key insight: "exactly k" = "at most k" − "at most k−1". This transforms an awkward exact constraint into two clean at-most windows.

Input: `nums = [1, 2, 1, 2, 3]`, `k = 2`

`subarraysWithAtmostKDistinct(nums, 2)` — windows with ≤ 2 distinct:

| right | nums[right] | curr | distinct | left | subarrays added | ans |
|-------|-------------|------|----------|------|-----------------|-----|
| 0     | 1           | `{1:1}`| 1        | 0    | 1               | 1   |
| 1     | 2           | `{1:1, 2:1}`| 2   | 0    | 2               | 3   |
| 2     | 1           | `{1:2, 2:1}`| 2   | 0    | 3               | 6   |
| 3     | 2           | `{1:2, 2:2}`| 2   | 0    | 4               | 10  |
| 4     | 3           | `{1:2, 2:2, 3:1}`| 3 > 2 → shrink to left=2| 2 | 3 | 13 |

`subarraysWithAtmostKDistinct(nums, 1)` = 3. Result = 13 - 3 = 10
