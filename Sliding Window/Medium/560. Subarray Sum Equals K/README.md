# 560. Subarray Sum Equals K

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/subarray-sum-equals-k/

## 1. Algorithm Used

Prefix sum with a complement hashmap — for each running prefix sum `curr`, we look up how many previous prefix sums equal `curr - k`, because any such prefix marks the start of a subarray that sums to exactly `k`.

## 2. How to Recognize the Pattern

- "number of subarrays with sum equal to k" with negative numbers possible → sliding window won't work (non-monotone) → prefix sum + hashmap.
- Count of subarrays, not just existence → need to accumulate counts, not just track seen/unseen.
- `prefix_hashmap[0] = 1` seed → handles subarrays that start at index 0 (where the prefix sum itself equals `k`).

## 3. Why This Algorithm Fits

- O(n) time — single pass; each element updates `curr` and performs one hashmap lookup and one insert.
- O(n) space — the hashmap stores at most n distinct prefix sums.
- Works with negative numbers and zeros, unlike a two-pointer approach which requires all-positive inputs.

## 4. How It Works

`curr` is the running prefix sum. At each element, `curr - k` is the prefix sum that a previous index would need to have so that the subarray from that index to the current one sums to `k`. We add `prefix_hashmap[curr - k]` to the answer (0 if the key is absent), then record `curr` in the map. The initial `prefix_hashmap[0] = 1` accounts for subarrays beginning at index 0.

```python
ans = curr = 0; prefix_hashmap = defaultdict(int); prefix_hashmap[0] = 1
for num in nums:
    curr += num
    ans += prefix_hashmap[curr - k]
    prefix_hashmap[curr] += 1
return ans
```

The order matters: look up `curr - k` before inserting `curr` — otherwise a subarray of length 0 (same start and end index) could be counted when `k == 0`.

Input: `nums = [1, 1, 1]`, `k = 2`

| num | curr | curr-k | prefix_hashmap[curr-k] | ans | prefix_hashmap |
|-----|------|--------|------------------------|-----|----------------|
| init | 0 | | | 0 | {0:1} |
| 1 | 1 | -1 | 0 | 0 | {0:1,1:1} |
| 1 | 2 | 0 | 1 | 1 | {0:1,1:1,2:1} |
| 1 | 3 | 1 | 1 | 2 | {0:1,1:1,2:1,3:1} |
| result | | | | 2 | |
