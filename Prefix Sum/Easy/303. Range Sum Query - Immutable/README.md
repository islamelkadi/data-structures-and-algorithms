# 303. Range Sum Query - Immutable

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/range-sum-query-immutable/

## 1. Algorithm Used

Precompute a prefix sum array so that any range sum query can be answered in O(1) using `prefix[right] - prefix[left-1]`.

## 2. How to Recognize the Pattern

- "Multiple queries on the same array" → repeated range sum lookups → precompute prefix sums once.
- "Sum of elements between index `left` and `right`" → contiguous subarray sum → prefix sum subtraction.
- Immutable array with many `sumRange` calls → O(n) build cost amortized across O(1) queries.

## 3. Why This Algorithm Fits

- O(n) time to build, O(1) per query — optimal when queries outnumber updates.
- O(n) space — one extra array of the same length as input.
- The key property: `sum(left, right) = prefix[right] - prefix[left-1]`, which reduces any range query to two array lookups.

## 4. How It Works

During initialization, build a prefix sum array where `prefix[i]` holds the cumulative sum of all elements from index 0 through i. For a query `(left, right)`, the answer is `prefix[right] - prefix[left-1]` — the total up to `right` minus everything before `left`. The `left == 0` edge case is handled separately since there is no `prefix[-1]`.

```python
# Init
self._prefix_sum = [nums[0]]
for i in range(1, len(nums)):
    self._prefix_sum.append(nums[i] + self._prefix_sum[-1])

# Query
def sumRange(self, left, right):
    if left == 0:
        return self._prefix_sum[right]
    return self._prefix_sum[right] - self._prefix_sum[left - 1]
```

The insight is that subtraction of two prefix values cancels out everything outside the window — no loop needed at query time.
