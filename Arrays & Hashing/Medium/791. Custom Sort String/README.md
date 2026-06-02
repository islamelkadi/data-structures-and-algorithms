# 791. Custom Sort String
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/custom-sort-string/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Frequency map with ordered reconstruction — place characters in the order defined by `order`, then append remaining characters.

## 2. How to Recognize the Pattern

- "sort a string according to a custom character order" → frequency map → reconstruct by iterating the order string.
- Characters not in `order` can appear in any position — append them at the end.

## 3. Why This Algorithm Fits

- O(n + m) time — O(n) to count s, O(m) to iterate order, O(k) for remaining chars (k ≤ 26).
- O(k) space — the frequency map holds at most 26 entries.
- Building the result from the order string guarantees the relative ordering constraint is met.

## 4. How It Works

Count the frequency of each character in s. Iterate through `order` and append each character the number of times it appears in s, removing it from the map. Then append any remaining characters (those not in `order`) in any order.

```python
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # There can be duplicates - a good question to ask
        frequency_s = Counter(s)

        str_ = ""
        for char in order: # this will preserve the order of the characters and you just perform a lookup below
            if char not in frequency_s:
                continue
            str_ += char * frequency_s[char]
            del frequency_s[char]
        
        for char, count in frequency_s.items():
            str_ += char * count
        
        return str_
```

Deleting from `frequency_s` after processing each character in `order` ensures the second loop only handles characters not covered by `order`, avoiding duplicates in the output.

Input: `order = "cba"`, `s = "abcd"`

| step | frequency_s | action | str_ |
|------|-------------|--------|------|
| build | `{'a':1, 'b':1, 'c':1, 'd':1}` | | |
| char = 'c' | `'c'` in `frequency_s` | append `"c"`, del `'c'` | `"c"` |
| char = 'b' | `'b'` in `frequency_s` | append `"b"`, del `'b'` | `"cb"` |
| char = 'a' | `'a'` in `frequency_s` | append `"a"`, del `'a'` | `"cba"` |
| remaining | `{'d':1}` | append `"d"` | `"cbad"` |
| result | | | `"cbad"` |
