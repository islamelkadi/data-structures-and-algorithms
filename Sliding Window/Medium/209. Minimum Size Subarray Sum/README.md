# 209. Minimum Size Subarray Sum

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/minimum-size-subarray-sum/

## 1. Algorithm Used

Variable sliding window that shrinks from the left whenever the running sum meets or exceeds `target`, minimising the window length at each valid state.

## 2. How to Recognize the Pattern

- "minimum length subarray with sum ≥ target" → contiguous subarray with a sum threshold → shrink-when-valid sliding window.
- All elements are positive → adding `nums[right]` always increases the sum, removing `nums[left]` always decreases it → window validity is monotone, making the two-pointer approach correct.
- Minimise length (not maximise) → record the answer inside the shrink loop, not after it.

## 3. Why This Algorithm Fits

- O(n) time — each element is added by `right` once and removed by `left` at most once.
- O(1) space — only three variables.
- The positive-integers constraint is essential: it guarantees that once `curr >= target`, shrinking from the left will eventually drop below the threshold, so the `while` loop always terminates.

## 4. How It Works

`curr` accumulates the sum of the current window. When `curr >= target` the window is valid — we record its length and then shrink by advancing `left` and subtracting `nums[left]`. We keep shrinking as long as the window remains valid, ensuring we find the minimum length for every valid right boundary.

```python
left = curr = 0; ans = float("inf")
for right in range(len(nums)):
    curr += nums[right]
    while curr >= target:
        ans = min(ans, right - left + 1)
        curr -= nums[left]; left += 1
return 0 if ans == float("inf") else ans
```

Returning 0 when `ans` is still infinity handles the case where no subarray reaches `target` — a clean sentinel check that avoids a separate pre-scan.
