# 2962. Count Subarrays Where Max Element Appears at Least K Times
**Difficulty:** Hard
**Link:** https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

## 1. Algorithm Used
Sliding window counting subarrays where the global max appears at least k times; count valid left boundaries using `res += left`.

## 2. How to Recognize the Pattern
- "count subarrays" + "global maximum appears at least k times" → fix right, find the smallest valid left, then all extensions to the left are also valid → sliding window with a left-boundary count.
- "at least k" with a fixed target value → shrink until the condition is just barely violated, then count.

## 3. Why This Algorithm Fits
- O(n) time — single pass, each element processed at most twice.
- O(1) space — only a count of max occurrences and two pointers.
- Once the window `[left, right]` has exactly k max elements, every subarray `[0..right], [1..right], ..., [(left-1)..right]` also satisfies "at least k", giving `left` valid subarrays ending at `right`.

## 4. How It Works
Track `max_count` as the number of times `max_val` appears in the current window. When `max_count >= k`, shrink from the left (decrementing `max_count` when a max element leaves) until the window has fewer than k max elements. At that point, all `left` possible left boundaries (indices 0 through left-1) form valid subarrays ending at `right`.

```python
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        left = max_count = res = 0
        for right in range(len(nums)):
            if nums[right] == max_val:
                max_count += 1
            while max_count >= k:
                if nums[left] == max_val:
                    max_count -= 1
                left += 1
            res += left
        return res
```

`res += left` works because after the shrink loop, `left` is the first index where the window `[left, right]` has fewer than k max elements — meaning all indices `0..left-1` as the start give a valid subarray ending at `right`.
