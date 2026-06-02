# 1512. Number of Good Pairs
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/number-of-good-pairs/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Notes & Lessons Learned](#5-notes--lessons-learned)

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

Input: `nums = [1, 2, 3, 1, 1, 3]`

| element | frequency | pairs = f*(f-1)//2 |
|---------|-----------|-------------------|
| 1 | 3 | 3*2//2 = 3 |
| 2 | 1 | 1*0//2 = 0 |
| 3 | 2 | 2*1//2 = 1 |
| total | | 4 |

## 5. Notes & Lessons Learned

> [!NOTE]
> **The picking-2 combination formula ($n \times (n-1) // 2$ or $C(n, 2)$)**:
> This is a fundamental formula in mathematics and computer science, frequently encountered in the following contexts:
>
> 1. **Combinatorics**: It is the formula for "combinations of 2 from n items" (often written as $^nC_2$ or $C(n,2)$).
> 2. **Graph Theory**: When calculating the maximum number of edges in an undirected graph with $n$ vertices (a complete graph).
> 3. **Array Processing**: When you need to count all possible unique pairs in an array.
> 4. **Triangular Numbers**: The sum of first $n-1$ natural numbers is $n \times (n-1) // 2$, which forms a triangular pattern.
>
> **Common Coding Problems using this formula**:
> - Counting the number of handshakes in a room of $n$ people.
> - Finding the number of unique pairs in an array.
> - Calculating diagonal elements in a matrix.
> - Network connectivity and route pairing problems.
