## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

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

Input: `nums = [2, 3, -1, 8, 4]`

| i | num | left_sum | right_sum = total-left_sum-num | equal? |
|---|-----|----------|-------------------------------|--------|
| — | — | total=16 | | |
| 0 | 2 | 0 | 16-0-2=14 | no → left_sum=2 |
| 1 | 3 | 2 | 16-2-3=11 | no → left_sum=5 |
| 2 | -1 | 5 | 16-5-(-1)=12 | no → left_sum=4 |
| 3 | 8 | 4 | 16-4-8=4 | yes → return 3 |
