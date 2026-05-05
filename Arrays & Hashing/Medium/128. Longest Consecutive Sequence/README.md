## 1. Algorithm Used

Hash Set with sequence-start detection.

## 2. How to Recognize the Pattern

- "Find the longest consecutive sequence" → need to identify connected runs of numbers.
- O(n log n) is easy with sorting, but the problem asks for O(n) → hash set for O(1) lookups.
- The key insight: only start counting from the beginning of a sequence (`num - 1` not in set). This avoids redundant work and keeps it O(n) overall.

## 3. Why This Algorithm Fits

- O(n) time — each number is visited at most twice (once in the loop, once in the while chain).
- O(n) space — for the set.
- Iterating over the set instead of the original array avoids processing duplicates.
- `subarr_len` is initialized inside the `if` block, so it resets correctly for each new sequence.

## 4. How It Works

Put all numbers in a set. For each number, check if it's the start of a sequence (`num - 1` not in set). If it is, walk forward with `num + 1` counting consecutive elements. Track the longest run found.

```python
nums_hashset = set(nums)
ans = 0
for num in nums_hashset:
    if num - 1 not in nums_hashset:
        subarr_len = 1
        while num + 1 in nums_hashset:
            subarr_len += 1
            num += 1
        ans = max(ans, subarr_len)
return ans
```

Input: `nums = [100, 4, 200, 1, 3, 2]` → set: `{1,2,3,4,100,200}`

| num | num-1 in set? | sequence walk | length | ans |
|-----|---------------|---------------|--------|-----|
| 100 | 99? no → start | 101? no | 1 | 1 |
| 4 | 3? yes → skip | — | — | 1 |
| 200 | 199? no → start | 201? no | 1 | 1 |
| 1 | 0? no → start | 2✓→3✓→4✓→5? no | 4 | 4 |
| 3 | 2? yes → skip | — | — | 4 |
| 2 | 1? yes → skip | — | — | 4 |