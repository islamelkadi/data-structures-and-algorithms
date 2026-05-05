# 152. Maximum Product Subarray

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/maximum-product-subarray/

## 1. Algorithm Used

Prefix and suffix product scan with zero-reset — scanning from both ends simultaneously handles negative-number pairs and zeros without tracking explicit min/max states.

## 2. How to Recognize the Pattern

- "maximum product subarray" → negatives can flip sign, zeros reset the product → need to consider subarrays ending at every position from both directions.
- Two negatives multiply to a positive → a suffix scan catches the case where the optimal subarray starts after an odd-count negative prefix.
- Zeros break any product to 0 → reset prefix/suffix to 1 when either hits 0, effectively starting a new subarray.

## 3. Why This Algorithm Fits

- O(n) time — single pass with two running products updated simultaneously.
- O(1) space — only four variables regardless of input size.
- The prefix+suffix trick is equivalent to tracking both the running maximum and minimum products but requires no explicit min tracking — the suffix naturally captures the "other side" of any negative pair.

## 4. How It Works

`prefix` accumulates the product left-to-right; `suffix` accumulates right-to-left. At each step `i`, `prefix` holds the product of `nums[0..i]` and `suffix` holds the product of `nums[n-1..n-1-i]`. Both are candidates for the answer. When either hits 0 (a zero element was included), it resets to 1 so the next element starts a fresh subarray.

```python
suffix = prefix = 1; ans = float("-inf"); n = len(nums)
for i in range(n):
    prefix *= nums[i]; suffix *= nums[n - i - 1]
    ans = max(ans, prefix, suffix)
    if prefix == 0: prefix = 1
    if suffix == 0: suffix = 1
return ans
```

Initialising `ans = float("-inf")` correctly handles all-negative arrays where the best product is a single negative number.

Input: `nums = [2, 3, -2, 4]`

| i | nums[i] | prefix | suffix | ans |
|---|---------|--------|--------|-----|
| 0 | 2 | 2 | 4 | 4 |
| 1 | 3 | 6 | -8 | 6 |
| 2 | -2 | -12 | -2 | 6 |
| 3 | 4 | -48→reset | 4→reset | 6 |
| result | | | | 6 |
