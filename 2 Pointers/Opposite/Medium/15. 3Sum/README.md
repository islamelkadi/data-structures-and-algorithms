# 15. 3Sum

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/3sum/

## 1. Algorithm Used

Sort + fix one element + opposite-direction two pointers on the remaining subarray; a set deduplicates triplets automatically.

## 2. How to Recognize the Pattern

- "Find all unique triplets that sum to zero" → reduce to 2Sum on a sorted array → fix one element, two-pointer scan for the other two.
- "No duplicate triplets" → sort first so equal values are adjacent, then deduplicate (here via a set).
- Brute force is O(n³). Sorting enables the two-pointer scan that brings it to O(n²).

## 3. Why This Algorithm Fits

- O(n²) time — O(n log n) to sort, then O(n) inner two-pointer scan for each of the n outer elements.
- O(n) space — the set of triplets (output size can be O(n²) in the worst case, but the set itself is bounded by the number of valid triplets).
- Sorting is the key enabler: once sorted, if the current sum is too small you advance `left`; if too large you retreat `right` — no element is revisited unnecessarily.

## 4. How It Works

Sort `nums`. For each index `i`, set `left = i + 1` and `right = len(nums) - 1`. Compute the three-way sum. If it equals 0, record the triplet. If the sum is less than 0, advance `left` to increase it; if greater than 0, retreat `right` to decrease it. Continue until `left` and `right` meet. The set ensures no duplicate triplets are returned regardless of repeated values in the input.

```python
nums.sort()
triplets = set()
for i in range(len(nums)):
    left, right = i + 1, len(nums) - 1
    while left < right:
        current_sum = nums[i] + nums[left] + nums[right]
        if current_sum == 0:
            triplets.add((nums[i], nums[left], nums[right]))
        if current_sum < 0:
            left += 1
        else:
            right -= 1
return list(triplets)
```

Using a set for deduplication is simpler than manually skipping duplicate values with pointer jumps, at the cost of a small amount of extra space.

Input: `nums = [-4, -1, -1, 0, 1, 2]` (after sort)

| i | nums[i] | left | right | sum | action |
|---|---------|------|-------|-----|--------|
| 0 | -4 | 1 | 5 | -4+-1+2=-3 | <0 → left++ |
| 0 | -4 | 2 | 5 | -4+-1+2=-3 | <0 → left++ |
| 0 | -4 | 3 | 5 | -4+0+2=-2 | <0 → left++ |
| 0 | -4 | 4 | 5 | -4+1+2=-1 | <0 → left++ |
| 0 | -4 | 5 | 5 | — | left>=right → next i |
| 1 | -1 | 2 | 5 | -1+-1+2=0 | ==0 → add (-1,-1,2) |
| 1 | -1 | 3 | 4 | -1+0+1=0 | ==0 → add (-1,0,1) |
| 1 | -1 | 4 | 4 | — | left>=right → next i |
| 2 | -1 | 3 | 5 | (dup of i=1, set handles it) | |
| 3 | 0 | 4 | 5 | 0+1+2=3 | >0 → right-- |
| 3 | 0 | 4 | 4 | — | left>=right → done |
| result | | | | | [(-1,-1,2), (-1,0,1)] |
