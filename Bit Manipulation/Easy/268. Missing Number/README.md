# 268. Missing Number

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/missing-number/

## 1. Algorithm Used

XOR all indices 0 through n together with all values in the array; every number that appears cancels itself out, leaving only the missing number.

## 2. How to Recognize the Pattern

- "Find the one missing number in a range 0..n" → XOR pairing → each present number cancels its index.
- O(1) space constraint rules out a frequency array or set → bit manipulation is the signal.
- "Array contains n distinct numbers from 0 to n" → exactly one value is unpaired → XOR isolates it.

## 3. Why This Algorithm Fits

- O(n) time — single pass over the array.
- O(1) space — accumulates the result in a single integer variable.
- XOR is self-inverse (`a ^ a = 0`) and commutative, so order doesn't matter and paired values vanish cleanly.

## 4. How It Works

Initialize `missing = len(nums)` to seed the XOR with `n` itself — this ensures the full range 0..n is represented on the index side. Then iterate with `enumerate`, XOR-ing each index `i` and each value `num` into `missing`. Every number that is present appears once as an index and once as a value, so it XORs to zero and drops out; the missing number has no matching value to cancel it.

```python
missing = len(nums)
for i, num in enumerate(nums):
    missing ^= i ^ num
return missing
```

Initializing with `len(nums)` rather than 0 is the key gotcha — it covers the case where `n` itself is the missing number, which would otherwise never appear as an index.

Input: `nums = [3, 0, 1]` (n=3, missing=2)

| i | nums[i] | missing ^= i ^ nums[i] | missing |
|---|---------|------------------------|---------|
| init | — | missing = 3 (len) | 3 = 011 |
| 0 | 3 | 011 ^ 000 ^ 011 | 000 |
| 1 | 0 | 000 ^ 001 ^ 000 | 001 |
| 2 | 1 | 001 ^ 010 ^ 001 | 010 = 2 |
| result | | | 2 ✓ |
