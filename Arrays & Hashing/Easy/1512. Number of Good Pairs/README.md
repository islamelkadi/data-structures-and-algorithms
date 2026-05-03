# 1512. Number of Good Pairs
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/number-of-good-pairs/

## 1. Algorithm Used

Frequency map with combinatorics — for each element with frequency f, there are f*(f-1)//2 valid pairs.

## 2. How to Recognize the Pattern

- "count pairs (i, j) where i < j and nums[i] == nums[j]" → frequency map → combination formula.
- Choosing 2 items from f identical items is the classic C(f, 2) = f*(f-1)//2 formula.

## 3. Why This Algorithm Fits

- O(n) time — one pass to build the counter, one pass over the distinct values.
- O(k) space — k is the number of distinct elements.
- The combination formula avoids an O(n²) nested loop entirely.

## 4. How It Works

Count the frequency of each element. For each frequency f, add f*(f-1)//2 to the result — this counts all pairs of indices that share the same value.

```python
from typing import List
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum(f * (f - 1) // 2 for f in freq.values())
```

The formula f*(f-1)//2 is equivalent to choosing 2 positions from f occurrences — it's the number of ways to pick an unordered pair without repetition.
