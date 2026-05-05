## 1. Algorithm Used

Prefix sum minimum tracking to find the required starting offset.

## 2. How to Recognize the Pattern

- "Step by step sum must always be positive" → the running prefix sum must never drop below 1 → find the minimum prefix sum.
- The start value is a constant offset added to every prefix sum → the worst case is the minimum prefix sum.
- "Minimum start value" → `max(1, 1 - min_prefix_sum)`.

## 3. Why This Algorithm Fits

- O(n) time — single pass to find the minimum prefix sum.
- O(1) space — only two variables: current running sum and the minimum seen.
- The start value shifts the entire prefix sum sequence up by a constant, so you only need to find how much to shift to keep the minimum at or above 1.

## 4. How It Works

Compute the running prefix sum while tracking the minimum value reached. The minimum prefix sum tells you the lowest point the cumulative total hits. To ensure every step stays ≥ 1, the start value must be at least `1 - min_prefix_sum`. The answer is at least 1 even if the prefix sum never goes negative.

```python
min_sum = curr = 0
for num in nums:
    curr += num
    min_sum = min(min_sum, curr)
return max(1, 1 - min_sum)
```

`max(1, ...)` handles the case where all prefix sums are positive — the minimum valid start value is always 1, never 0 or negative.

Input: `nums = [-3, 2, -3, 4, 2]`

| i | num | curr | min_sum |
|---|-----|------|---------|
| 0 | -3 | -3 | -3 |
| 1 | 2 | -1 | -3 |
| 2 | -3 | -4 | -4 |
| 3 | 4 | 0 | -4 |
| 4 | 2 | 2 | -4 |
| result | | | max(1, 1-(-4)) = 5 |
