# 1695. Maximum Erasure Value
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/maximum-erasure-value/

## 1. Algorithm Used
Variable-size sliding window with a set to enforce uniqueness; maximize the running sum.

## 2. How to Recognize the Pattern
- "subarray with unique elements" + "maximize sum" → uniqueness constraint on a window → variable sliding window + set.
- Need to both track membership (set) and maintain a running total (curr_sum) to avoid O(n) recomputation on each shrink.

## 3. Why This Algorithm Fits
- O(n) time — each element enters and leaves the window at most once.
- O(n) space — the set holds at most all distinct elements.
- Maintaining `curr_sum` incrementally avoids recomputing the window sum from scratch on every shrink step.

## 4. How It Works
Before adding `nums[right]`, evict elements from the left until the duplicate is removed, subtracting each from `curr_sum`. Then add `nums[right]` to both the set and `curr_sum`, and update the result.

```python
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = curr_sum = res = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            curr_sum += nums[right]
            res = max(res, curr_sum)
        return res
```

The shrink loop runs before adding `nums[right]`, ensuring the set never contains a duplicate at the point of insertion.
