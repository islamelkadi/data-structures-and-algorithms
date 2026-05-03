## 1. Algorithm Used

Prefix product left-to-right pass followed by suffix product right-to-left pass, combined in-place.

## 2. How to Recognize the Pattern

- "Product of all elements except self" without using division → can't just divide total by element → need prefix and suffix products.
- O(n) time and O(1) extra space constraint → can't store separate prefix and suffix arrays → build result in two passes over the output array itself.
- Each output element is the product of everything to its left times everything to its right → two independent passes.

## 3. Why This Algorithm Fits

- O(n) time — two linear passes, no nested loops.
- O(1) extra space — the output array doesn't count; only two scalar accumulators are used.
- Division is explicitly forbidden by the problem, making the two-pass prefix/suffix approach the canonical solution.

## 4. How It Works

First pass (left to right): fill `result[i]` with the product of all elements to the left of i. Use a running `prefix` scalar, starting at 1. Second pass (right to left): multiply each `result[i]` by the product of all elements to the right of i, using a running `suffix` scalar starting at 1.

```python
n = len(nums)
result = [1] * n
prefix = 1
for i in range(n):
    result[i] = prefix
    prefix *= nums[i]
suffix = 1
for i in range(n - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]
return result
```

After the first pass, `result[i]` holds the left product. The second pass multiplies in the right product, completing each position without ever needing a separate suffix array.
