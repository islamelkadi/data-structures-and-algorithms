# 325. Maximum Size Subarray Sum Equals k

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

## 1. Algorithm Used

Running prefix sum combined with a hashmap to find, in O(n), the longest subarray whose elements sum to exactly k.

## 2. How to Recognize the Pattern

- "Subarray sum equals k" → prefix sum difference → hashmap lookup for `prefix_sum - k`.
- "Maximum length" (not count) → store the *first* occurrence of each prefix sum to maximize the distance.
- Array contains negative numbers or zeros → sliding window won't work; prefix sum + hashmap is the right tool.

## 3. Why This Algorithm Fits

- O(n) time — single pass with O(1) hashmap operations.
- O(n) space — hashmap stores at most one entry per index.
- Storing only the first occurrence of each prefix sum guarantees the widest possible subarray when a match is found.

## 4. How It Works

Maintain a running `prefix_sum` as you scan left to right. At each index `right`, check whether `prefix_sum - k` has been seen before; if so, the subarray from just after that earlier index to `right` sums to k, and its length is `right - curr[prefix_sum - k]`. Initializing `curr = {0: -1}` handles the case where the subarray starts at index 0 (the entire prefix sums to k). Only the first occurrence of each prefix sum is recorded so that the subarray length is maximized.

```python
prefix_sum = ans = 0
curr = {0: -1}
for right in range(len(nums)):
    prefix_sum += nums[right]
    if prefix_sum not in curr:
        curr[prefix_sum] = right
    seen = prefix_sum - k
    if seen in curr:
        ans = max(ans, right - curr[seen])
return ans
```

The `{0: -1}` seed is the key gotcha — without it, subarrays that start at index 0 are silently missed.

Input: `nums = [1, -1, 5, -2, 3]`, `k = 3`

| right | nums[right] | prefix_sum | in curr? | seen = ps-k | ans |
|-------|-------------|------------|----------|-------------|-----|
| init | | 0 | {0:-1} | | 0 |
| 0 | 1 | 1 | no→store | 1-3=-2, not in curr | 0 |
| 1 | -1 | 0 | 0 in curr (-1)! | 0-3=-3, not in curr | 0 |
| 2 | 5 | 5 | no→store | 5-3=2, not in curr | 0 |
| 3 | -2 | 3 | no→store | 3-3=0, in curr (-1) → len=3-(-1)=4 | 4 |
| 4 | 3 | 6 | no→store | 6-3=3, in curr (3) → len=4-3=1 | 4 |
| result | | | | | 4 |
