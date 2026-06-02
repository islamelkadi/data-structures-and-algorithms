# 771. Jewels and Stones

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/jewels-and-stones/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

HashMap / Set frequency lookup. We convert `jewels` to a set for O(1) membership checking and use `Counter` to get frequency counts of characters in `stones`.

## 2. How to Recognize the Pattern

- "how many of the stones you have are also jewels" → counting target elements from a set in a collection → hash set + hash map.
- Membership lookup is required to check if a stone is a jewel, and count is required to determine the stone frequency.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(J + S) where J is the length of `jewels` and S is the length of `stones`. Creating the set is O(J), counting stones is O(S), and iterating unique jewels is at most O(J) with O(1) count lookups.
- **Space Complexity**: O(J + S) to store the set of jewels and the count of stones. Since alphabet sizes are bounded (at most 52 English letters), it is O(1) auxiliary space.
- A brute force nested-loop check would take O(J * S) time, making hashset/hashmap approach much more efficient.

## 4. How It Works

1. Convert `jewels` into a set `jewels_hashset` to remove any potential duplicate characters and enable O(1) lookup.
2. Build a frequency count of characters in `stones` using `Counter` (`stones_hashmap`).
3. Iterate through each character `jewel` in `jewels_hashset` and add its count from `stones_hashmap` to `summation`.
4. Return `summation`.

```python
from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_hashset = set(jewels)
        stones_hashmap = Counter(stones)
        summation = 0
        for jewel in jewels_hashset:
            summation += stones_hashmap.get(jewel, 0)
        return summation
```

### Dry Run Table
Input: `jewels = "aA"`, `stones = "aAAbbbb"`

`jewels_hashset` = `{'a', 'A'}`
`stones_hashmap` = `{'a': 1, 'A': 2, 'b': 4}`

| jewel | stones_hashmap.get(jewel, 0) | summation comparison | summation |
|-------|------------------------------|----------------------|-----------|
| *init*| -                            | -                    | 0         |
| 'a'   | 1                            | `0 + 1 = 1`          | 1         |
| 'A'   | 2                            | `1 + 2 = 3`          | 3         |

Result: `3`
