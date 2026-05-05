## 1. Algorithm Used

Prefix sum with hashmap frequency count to find subarrays with an exact sum.

## 2. How to Recognize the Pattern

- "Count subarrays with sum equal to goal" → prefix sum + hashmap (same pattern as subarray sum equals k).
- Binary array with a target sum → prefix sum grows monotonically, but hashmap approach works for any values.
- Exact count of subarrays → `prefix_count[curr_sum - goal]` gives the number of valid left endpoints.

## 3. Why This Algorithm Fits

- O(n) time — single pass, O(1) hashmap lookup per element.
- O(n) space — the hashmap stores at most n+1 distinct prefix sums.
- The complement trick (`curr_sum - goal`) converts "find subarray with sum == goal" into "find a previous prefix sum that differs from the current by exactly goal".

## 4. How It Works

Maintain a running prefix sum and a hashmap counting how many times each prefix sum has been seen. For each new element, check how many previous positions had prefix sum equal to `curr_sum - goal` — each such position forms a valid subarray ending here. Seed the map with `{0: 1}` to handle subarrays starting from index 0.

```python
prefix_count = defaultdict(int)
prefix_count[0] = 1
curr_sum = count = 0
for num in nums:
    curr_sum += num
    count += prefix_count[curr_sum - goal]
    prefix_count[curr_sum] += 1
return count
```

The `prefix_count[0] = 1` initialization is critical — it accounts for subarrays that start at index 0 and whose sum equals the goal exactly.

Input: `nums = [1, 0, 1, 0, 1]`, `goal = 2`

| num | curr_sum | curr-goal | prefix_count[curr-goal] | count | prefix_count |
|-----|----------|-----------|-------------------------|-------|--------------|
| init | 0 | | | 0 | {0:1} |
| 1 | 1 | -1 | 0 | 0 | {0:1,1:1} |
| 0 | 1 | -1 | 0 | 0 | {0:1,1:2} |
| 1 | 2 | 0 | 1 | 1 | {0:1,1:2,2:1} |
| 0 | 2 | 0 | 1 | 2 | {0:1,1:2,2:2} |
| 1 | 3 | 1 | 2 | 4 | {0:1,1:2,2:2,3:1} |
| result | | | | 4 | |
