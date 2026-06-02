## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Notes & Lessons Learned](#5-notes--lessons-learned)

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

Input: `nums = [1, 1, 2, 1, 1]`, `k = 3`

| num | num%2 | curr | curr-k | prefix_count[curr-k] | count | prefix_count |
|-----|-------|------|--------|----------------------|-------|--------------|
| init | | 0 | | | 0 | {0:1} |
| 1 | 1 | 1 | -2 | 0 | 0 | {0:1,1:1} |
| 1 | 1 | 2 | -1 | 0 | 0 | {0:1,1:1,2:1} |
| 2 | 0 | 2 | -1 | 0 | 0 | {0:1,1:1,2:2} |
| 1 | 1 | 3 | 0 | 1 | 1 | {0:1,1:1,2:2,3:1} |
| 1 | 1 | 4 | 1 | 1 | 2 | {0:1,1:1,2:2,3:1,4:1} |
| result | | | | | 2 | |

## 5. Notes & Lessons Learned

> [!NOTE]
> **Difference Between "Max Size Subarray" vs "Count Subarrays"**:
> - **Max Size (e.g., Problem 325)**: We want the maximum size of a subarray summing to $k$. In this case, we store the *earliest index* of each prefix sum in the hash map and measure index differences (`right - seen[prefix_sum - k]`).
> - **Count Subarrays (this problem)**: We want to find the *number* of valid subarrays. Thus, we use the hash map to count the *frequency of occurrences* of each prefix sum. When `prefix_sum - k` is found in our frequency map, we add `prefix_count[prefix_sum - k]` to our running total.
>
> **Significance of `curr[0] = 1`**:
> We initialize the frequency map with `prefix_count[0] = 1` (meaning "we have seen zero odd numbers once" at the start). This is critical to ensure that any valid subarray starting at index `0` is properly counted when `prefix_sum` exactly equals $k$.
>
> **Alternative Sliding Window Approach (At-Most-$K$)**:
> We can also solve this using the **at-most-$K$** sliding window pattern:
> $$\text{exactly}(K) = \text{at\_most}(K) - \text{at\_most}(K - 1)$$
> Here, `at_most(k)` finds the number of subarrays with at most $k$ odd numbers in $O(N)$ time and $O(1)$ space:
>
> ```python
> def numberOfSubarrays(self, nums: List[int], k: int) -> int:
>     def numberOfAtMostSubarrays(nums, k):
>         left = curr = ans = 0
>         for right in range(len(nums)):
>             curr += nums[right] % 2
>             while curr > k and left <= right:
>                 curr -= nums[left] % 2
>                 left += 1
>             ans += right - left + 1
>         return ans
>     return numberOfAtMostSubarrays(nums, k) - numberOfAtMostSubarrays(nums, k - 1)
> ```
