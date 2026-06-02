# 1493. Longest Subarray of 1s After Deleting One Element
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Notes & Lessons Learned](#5-notes--lessons-learned)

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

Input: `nums = [1, 1, 0, 1]`

| right | nums[right] | zeros | left | res = right-left |
|-------|-------------|-------|------|------------------|
| 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 2 | 0 | 1 | 0 | 2 |
| 3 | 1 | 1 | 0 | 3 |
| result | | | | 3 |

## 5. Notes & Lessons Learned

> [!NOTE]
> **Edge Case Verification & Destructive Set Pops**:
> When optimizing early exits for uniform inputs:
> - **All-Ones**: If `nums_hashset == {1}`, deleting one element means returning `len(nums) - 1`.
> - **All-Zeros**: If `nums_hashset == {0}`, deleting one element leaves no `1`s, so we must return `0`.
>
> **Pitfall**: Avoid using `nums_hashset.pop() == 1` inside conditional checks. `pop()` is destructive and mutates the set, which will cause subsequent checks to see an empty or altered set. Always compare sets directly (e.g. `nums_hashset == {1}`).
>
> **Window Sizing for Mandatory Deletion**:
> In standard sliding window problems, the size of a window `[left, right]` is `right - left + 1`. Because this problem demands the deletion of exactly one element, we subtract 1 from the size, yielding:
> $$\text{Window Size} = (right - left + 1) - 1 = right - left$$
> This handles both the zero-deletion (when a zero is present in the window) and case when no zeros exist in the window (where we still must delete one element).
