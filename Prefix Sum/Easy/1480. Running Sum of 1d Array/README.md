## 1. Algorithm Used

In-place prefix sum accumulation.

## 2. How to Recognize the Pattern

- "Running sum" or "cumulative sum" in the problem title → direct prefix sum construction.
- Each output element depends on all previous input elements → prefix sum.
- Allowed to modify the input array → in-place accumulation, O(1) extra space.

## 3. Why This Algorithm Fits

- O(n) time — single left-to-right pass.
- O(1) space — result is built in-place by overwriting the input array.
- Each element only needs the value immediately before it, so no auxiliary array is required.

## 4. How It Works

Starting at index 1, add the previous element to the current element. Each `nums[i]` becomes the sum of all original elements from index 0 through i. The first element is already its own running sum and needs no change.

```python
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]
return nums
```

Because each position only looks one step back, the in-place update is safe — by the time you reach index i, `nums[i-1]` already holds the correct prefix sum.
