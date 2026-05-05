# 487. Max Consecutive Ones II

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/max-consecutive-ones-ii/

## 1. Algorithm Used

Variable sliding window with a zero budget of 1 — the window may contain at most one zero, and shrinks from the left when a second zero is encountered.

## 2. How to Recognize the Pattern

- "flip at most one 0 to 1, find longest run" → at-most-k zeros window → sliding window with a zero counter.
- Budget of 1 → shrink when `zero_counter > 1`, identical structure to 485 (budget 0) and 1004 (budget k).
- This is the middle problem in the consecutive-ones trilogy: 485 → 487 → 1004.

## 3. Why This Algorithm Fits

- O(n) time — each element is visited by `right` once and by `left` at most once.
- O(1) space — only three integer variables.
- The generalised zero-budget pattern means changing the single constant `1` to `k` solves 1004 (Max Consecutive Ones III) with no other modifications.

Input: `nums = [1, 0, 1, 1, 0]`

| right | nums[right] | zero_counter | left | window size | res |
|-------|-------------|--------------|------|-------------|-----|
| 0 | 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 2 | 2 |
| 2 | 1 | 1 | 0 | 3 | 3 |
| 3 | 1 | 1 | 0 | 4 | 4 |
| 4 | 0 | 2>1 → shrink: left=2 (0 leaves) | 2 | 3 | 4 |

## 4. How It Works

`zero_counter` tracks zeros inside the current window. When `nums[right]` is 0 the budget increments. If `zero_counter` exceeds 1, we shrink from `left`: if `nums[left]` was a zero we decrement the counter, then advance `left`. Once the budget is back within limit the window `[left, right]` contains at most one zero and we update the maximum length.

```python
left = zero_counter = max_array_len = 0
for right in range(len(nums)):
    if nums[right] == 0:
        zero_counter += 1
    while zero_counter > 1:
        if nums[left] == 0: zero_counter -= 1
        left += 1
    max_array_len = max(max_array_len, right - left + 1)
return max_array_len
```

The window length `right - left + 1` always counts the flipped zero as part of the run — the algorithm never needs to explicitly track which zero was flipped.
