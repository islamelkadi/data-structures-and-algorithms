# 2958. Length of Longest Subarray With at Most K Frequency
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

## 1. Algorithm Used
Variable-size sliding window with a frequency hashmap; shrink when any element exceeds frequency k.

## 2. How to Recognize the Pattern
- "longest subarray" + "frequency of each element at most k" → maximize window under a per-element frequency constraint → variable sliding window + hashmap.
- Only the newly added element (`nums[right]`) can violate the constraint, so the shrink condition is simple.

## 3. Why This Algorithm Fits
- O(n) time — each element enters and leaves the window at most once.
- O(n) space — frequency map holds at most all distinct elements.
- Because only `nums[right]` can push a frequency over k, we only need to check that one entry when deciding to shrink.

## 4. How It Works
Expand right, incrementing `freq[nums[right]]`. If that frequency exceeds k, shrink from the left until it's back within bounds. Track the maximum window length seen.

```python
from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = res = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
```

Only `nums[right]`'s frequency is checked in the while condition — no other element can newly violate the constraint when right advances.

Input: `nums = [1, 2, 3, 1, 2, 3, 1, 2]`, `k = 2`

| right | nums[right] | freq | freq[nums[right]]>k? | left | res |
|-------|-------------|------|----------------------|------|-----|
| 0 | 1 | {1:1} | no | 0 | 1 |
| 1 | 2 | {1:1,2:1} | no | 0 | 2 |
| 2 | 3 | {1:1,2:1,3:1} | no | 0 | 3 |
| 3 | 1 | {1:2,2:1,3:1} | no | 0 | 4 |
| 4 | 2 | {1:2,2:2,3:1} | no | 0 | 5 |
| 5 | 3 | {1:2,2:2,3:2} | no | 0 | 6 |
| 6 | 1 | {1:3,…} | yes → shrink: left=1 (1 leaves→{1:2}) | 1 | 6 |
| 7 | 2 | {1:2,2:3,3:2} | yes → shrink: left=2 (2 leaves→{2:2}) | 2 | 6 |
