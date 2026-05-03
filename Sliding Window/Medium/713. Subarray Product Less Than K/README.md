# 713. Subarray Product Less Than K
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/subarray-product-less-than-k/

## 1. Algorithm Used
Variable-size sliding window; shrink left when product >= k.

## 2. How to Recognize the Pattern
- "contiguous subarray" + "product less than k" → count subarrays satisfying a multiplicative constraint → variable sliding window.
- Product can grow and shrink as the window expands/contracts, making a two-pointer approach viable.

## 3. Why This Algorithm Fits
- O(n) time — each element is added and removed at most once.
- O(1) space — only a running product and two pointers.
- Multiplying in new elements and dividing out old ones keeps the product current without recomputation.

## 4. How It Works
Expand the right pointer, multiplying the new element into `product`. Whenever `product >= k`, divide out `nums[left]` and advance `left` until the window is valid again. Every valid window ending at `right` contributes `right - left + 1` subarrays (all subarrays ending at `right` with any left boundary in `[left, right]`).

```python
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        product, left, count = 1, 0, 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        return count
```

The `k <= 1` guard handles the edge case where no positive-integer product can ever be less than k.
