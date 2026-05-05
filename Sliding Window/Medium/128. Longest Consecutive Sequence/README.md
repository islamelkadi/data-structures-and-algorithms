# 128. Longest Consecutive Sequence

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/longest-consecutive-sequence/

## 1. Algorithm Used

Hash set with sequence-start detection — only begin counting a run from `num` when `num - 1` is absent from the set, ensuring each sequence is counted exactly once.

## 2. How to Recognize the Pattern

- "longest consecutive sequence" with O(n) time requirement → sorting is too slow → hash set for O(1) membership.
- Need to avoid re-counting the same sequence from every element → only start from the smallest element of each run (where `num - 1` is not in the set).
- No subarray/contiguous constraint on indices, only on values → sliding window on values, not indices.

## 3. Why This Algorithm Fits

- O(n) time — building the set is O(n); each element is the start of at most one sequence, and the inner `while` loop across all sequences visits each element at most once total.
- O(n) space — the hash set stores all unique values.
- The sequence-start guard (`num - 1 not in set`) is what collapses the naive O(n²) approach into O(n).

## 4. How It Works

We load all numbers into a set for O(1) lookup. For each number, we skip it if `num - 1` is in the set (it's not a sequence start). Otherwise we walk forward with `num + 1`, `num + 2`, … counting the run length until we fall off the end of the sequence, then update the answer.

```python
nums_hashset = set(nums)
ans = 0
for num in nums_hashset:
    if num - 1 not in nums_hashset:
        subarr_len = 1
        while num + 1 in nums_hashset:
            subarr_len += 1; num += 1
        ans = max(ans, subarr_len)
return ans
```

Iterating over `nums_hashset` rather than `nums` automatically deduplicates, so duplicate values in the input don't cause incorrect counts or extra work.

Input: `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]` → set: `{0,1,2,3,4,5,6,7,8}`

| num | num-1 in set? | sequence walk | length | ans |
|-----|---------------|---------------|--------|-----|
| 0 | -1? no → start | 1✓→2✓→3✓→4✓→5✓→6✓→7✓→8✓→9? no | 9 | 9 |
| 3 | 2? yes → skip | — | — | 9 |
| 7 | 6? yes → skip | — | — | 9 |
| others | all have num-1 in set → skip | | | 9 |
