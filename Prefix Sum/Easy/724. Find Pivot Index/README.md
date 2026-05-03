## 1. Algorithm Used

Prefix sum with derived suffix: pivot where left sum equals right sum.

## 2. How to Recognize the Pattern

- "Find an index where the sum of elements to the left equals the sum to the right" → pivot index → prefix sum + derived suffix.
- You need both a left aggregate and a right aggregate at each position → compute total once, derive the right side as `total - left_sum - nums[i]`.
- Brute force recomputes sums for every index (O(n²)); a single running total brings it to O(n).

## 3. Why This Algorithm Fits

- O(n) time — one pass for the total, one pass to find the pivot.
- O(1) space — only two variables tracked alongside the loop.
- The right sum never needs to be stored explicitly: `right_sum = total - left_sum - nums[i]`.

## 4. How It Works

Compute the total sum of the array. Walk left to right, maintaining a running `left_sum`. At each index, the right sum is `total - left_sum - nums[i]`. If `left_sum == right_sum`, that index is the pivot. After checking, add `nums[i]` to `left_sum` and continue.

```python
total = sum(nums)
left_sum = 0
for i, num in enumerate(nums):
    if left_sum == total - left_sum - num:
        return i
    left_sum += num
return -1
```

The key insight is that you never need to store the right side — it's always derivable from the total and the current left accumulation.
