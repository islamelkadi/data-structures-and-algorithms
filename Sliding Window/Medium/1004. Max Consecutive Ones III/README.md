# 1004. Max Consecutive Ones III
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/max-consecutive-ones-iii/

## 1. Algorithm Used
Variable-size sliding window with a "zero budget" of k; shrink when zeros in the window exceed k.

## 2. How to Recognize the Pattern
- "flip at most k zeros" + "longest subarray of 1s" → treat flipped zeros as a budget → variable sliding window.
- "at most k" constraint on a binary array → classic zero-budget window pattern.

## 3. Why This Algorithm Fits
- O(n) time — each element is visited at most twice (once by right, once by left).
- O(1) space — only a zero counter and two pointers.
- The window invariant is simple: count of zeros ≤ k.

## 4. How It Works
Expand right, counting zeros. When `zeros > k`, shrink from the left, decrementing the zero count when a zero leaves the window. The maximum valid window length is the answer.

```python
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zeros = res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
```

This is the general form of 1493 (Longest Subarray of 1s After Deleting One Element), which is just this problem with k=1 and a mandatory deletion.
