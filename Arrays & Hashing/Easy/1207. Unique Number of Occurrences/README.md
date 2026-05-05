# 1207. Unique Number of Occurrences
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/unique-number-of-occurrences/

## 1. Algorithm Used

Frequency map with a uniqueness check on the frequency values using a set.

## 2. How to Recognize the Pattern

- "check if occurrence counts are all different" → build a frequency map → compare value count to set size.
- If converting the frequency values to a set reduces the count, there are duplicates.

## 3. Why This Algorithm Fits

- O(n) time — one pass to build the counter, one pass to build the set.
- O(k) space — k is the number of distinct elements.
- Set size vs dict size comparison is a clean O(1) uniqueness check.

## 4. How It Works

Count the frequency of each element with a Counter. Then compare the number of frequency values to the number of unique frequency values — if they match, all occurrences are unique.

```python
from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        return len(freq.values()) == len(set(freq.values()))
```

The comparison `len(freq.values()) == len(set(freq.values()))` is the idiomatic way to check for duplicates in any collection.

Input: `arr = [1, 2, 2, 1, 1, 3]`

| step | freq | freq.values() | set(values) | len match? |
|------|------|---------------|-------------|------------|
| build | {1:3, 2:2, 3:1} | [3, 2, 1] | {3, 2, 1} | 3==3 → True |
