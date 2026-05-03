# 1493. Longest Subarray of 1s After Deleting One Element
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

## 1. Algorithm Used
Variable-size sliding window tracking zeros; allow at most 1 zero (representing the deleted element).

## 2. How to Recognize the Pattern
- "delete one element" + "longest subarray of 1s" → the deleted slot acts as a single allowed zero → variable sliding window with a zero budget of 1.
- Equivalent to: find the longest window with at most one 0, then subtract 1 for the mandatory deletion.

## 3. Why This Algorithm Fits
- O(n) time — single pass with two pointers.
- O(1) space — only a zero counter and two pointers.
- The problem reduces to 1004. Max Consecutive Ones III with k=1, minus 1 from the result.

## 4. How It Works
Expand right, counting zeros. When `zeros > 1`, shrink from the left until the window has at most one zero. The answer is `right - left` (not `+1`) because one element must always be deleted — the window length minus the mandatory deletion.

```python
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = zeros = res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left)  # -1 because we must delete one element
        return res
```

The key insight: `right - left` instead of `right - left + 1` accounts for the one element that must be deleted from the window.
