## 1. Algorithm Used

Prefix sum with derived suffix: find the leftmost index where left sum equals right sum.

## 2. How to Recognize the Pattern

- "Find an index where the sum of elements to the left equals the sum to the right" → same pattern as pivot index (724).
- Requires both a left and right aggregate at each position → compute total once, derive right side on the fly.
- "Leftmost" qualifier → return on the first match found scanning left to right.

## 3. Why This Algorithm Fits

- O(n) time — one pass for the total, one pass to find the middle index.
- O(1) space — only a running left sum and the precomputed total are needed.
- Identical logic to 724. Find Pivot Index — the problems are equivalent.

## 4. How It Works

Compute the total sum. Walk left to right with a running `left_sum`. At each index i, the right sum is `total - left_sum - nums[i]`. If they match, return i immediately (leftmost wins). Otherwise, add `nums[i]` to `left_sum` and continue.

```python
total = sum(nums)
left_sum = 0
for i, num in enumerate(nums):
    if left_sum == total - left_sum - num:
        return i
    left_sum += num
return -1
```

This problem is functionally identical to 724. Find Pivot Index — the same one-pass prefix sum approach solves both.
