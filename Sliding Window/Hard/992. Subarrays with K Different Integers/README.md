# 992. Subarrays with K Different Integers
**Difficulty:** Hard
**Link:** https://leetcode.com/problems/subarrays-with-k-different-integers/

## 1. Algorithm Used
at-most-k trick: answer = atMost(k) - atMost(k-1), where atMost counts subarrays with at most k distinct integers.

## 2. How to Recognize the Pattern
- "exactly k distinct" → direct sliding window is hard because the window can't stay "exactly k" cleanly → reframe as atMost(k) - atMost(k-1).
- Whenever a problem asks for "exactly k" of something countable, consider the at-most subtraction trick.

## 3. Why This Algorithm Fits
- O(n) time — two linear passes (atMost called twice).
- O(k) space — frequency map holds at most k+1 distinct keys before shrinking.
- atMost(k) is easy to implement with a standard variable window; the subtraction isolates the "exactly k" case.

## 4. How It Works
`atMost(k)` counts all subarrays with ≤ k distinct integers using a frequency map. When `len(freq) > k`, shrink from the left, deleting entries that reach zero frequency. Each valid right position contributes `right - left + 1` subarrays. Subtracting `atMost(k-1)` from `atMost(k)` leaves only subarrays with exactly k distinct integers.

```python
from typing import List
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            freq = defaultdict(int)
            left = res = 0
            for right in range(len(nums)):
                freq[nums[right]] += 1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                res += right - left + 1
            return res
        return atMost(k) - atMost(k - 1)
```

The key insight: "exactly k" = "at most k" − "at most k−1". This transforms an awkward exact constraint into two clean at-most windows.

Input: `nums = [1, 2, 1, 2, 3]`, `k = 2`

atMost(2) — windows with ≤ 2 distinct:

| right | nums[right] | freq | distinct | left | subarrays added | res |
|-------|-------------|------|----------|------|-----------------|-----|
| 0 | 1 | {1:1} | 1 | 0 | 1 | 1 |
| 1 | 2 | {1:1,2:1} | 2 | 0 | 2 | 3 |
| 2 | 1 | {1:2,2:1} | 2 | 0 | 3 | 6 |
| 3 | 2 | {1:2,2:2} | 2 | 0 | 4 | 10 |
| 4 | 3 | {1:2,2:2,3:1} | 3>2 → shrink to left=2 | 2 | 3 | 13 |

atMost(1) = 3. Result = 13 - 3 = 10
