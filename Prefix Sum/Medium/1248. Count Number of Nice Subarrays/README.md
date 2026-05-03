## 1. Algorithm Used

Prefix sum of odd-number counts with hashmap frequency tracking to count subarrays with exactly k odd numbers.

## 2. How to Recognize the Pattern

- "Count subarrays with exactly k odd numbers" → reduce to "subarray sum equals k" by mapping odd → 1, even → 0.
- Exact count of subarrays with a property → prefix sum + hashmap complement trick.
- `num % 2` converts each element to 0 or 1, turning the problem into a binary subarray sum problem identical to 930.

## 3. Why This Algorithm Fits

- O(n) time — single pass with O(1) hashmap operations.
- O(n) space — hashmap holds at most n+1 distinct prefix counts.
- The `num % 2` transformation is the only difference from 930. Binary Subarrays with Sum — the underlying algorithm is identical.

## 4. How It Works

Track a running count of odd numbers seen so far (`curr`). Use a hashmap to count how many times each prefix odd-count has occurred. For each element, the number of valid subarrays ending here is `prefix_count[curr - k]` — the number of earlier positions where the odd count was exactly k less than now. Seed with `{0: 1}` for subarrays starting at index 0.

```python
prefix_count = defaultdict(int)
prefix_count[0] = 1
curr = count = 0
for num in nums:
    curr += num % 2
    count += prefix_count[curr - k]
    prefix_count[curr] += 1
return count
```

`num % 2` is the key reduction — it strips away the actual values and keeps only the parity, transforming an "odd numbers" problem into a standard prefix sum problem.
