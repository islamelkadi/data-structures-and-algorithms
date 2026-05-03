## 1. Algorithm Used

Two-pass prefix/suffix product with constant extra space.

## 2. How to Recognize the Pattern

- "Product of array except self, no division" → need the product of everything before and everything after each index.
- That's prefix and suffix products — classic two-pass pattern.
- The O(1) space optimization: use the output array for one pass, a running variable for the other.

## 3. Why This Algorithm Fits

- Two separate passes cleanly separate the prefix and suffix concerns.
- The output array stores prefix products first, then gets multiplied by suffix products in-place — no extra arrays needed.
- Division is banned, so you can't just do `total_product / nums[i]`. The two-pass approach avoids division entirely.

## 4. How It Works

First pass (left to right): store the running prefix product at each index — `result[i]` = product of everything before `i`. Second pass (right to left): multiply each `result[i]` by the running suffix product — product of everything after `i`. Each index ends up with `prefix × suffix` = product of array except self.

```python
result = [1] * len(nums)

prefix = 1
for i in range(len(nums)):
    result[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(len(nums) - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]

return result
```

Visualization with `nums = [1, 2, 3, 4]`:

```
Left pass:  result = [1, 1, 2, 6]     ← product of everything before each index
Right pass: result = [24, 12, 8, 6]   ← multiplied by product of everything after

  index 0: 1 × 24 = 24  (nothing before × 2*3*4)
  index 1: 1 × 12 = 12  (1 × 3*4)
  index 2: 2 × 4  = 8   (1*2 × 4)
  index 3: 6 × 1  = 6   (1*2*3 × nothing after)
```

## 5. Time & Space Complexity

Time: O(n) — two passes through the array, O(1) work per element.

Space: O(1) extra — the output array doesn't count per the problem's rules. Only `prefix` and `suffix` variables are used beyond that.