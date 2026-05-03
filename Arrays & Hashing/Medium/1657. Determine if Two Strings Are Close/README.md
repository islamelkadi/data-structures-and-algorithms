# 1657. Determine if Two Strings Are Close
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/determine-if-two-strings-are-close/

## 1. Algorithm Used

Two-condition frequency comparison — same character sets and same multiset of frequency values.

## 2. How to Recognize the Pattern

- "can you transform one string into another by swapping or remapping characters" → check structural equivalence of frequency distributions.
- Two strings are "close" if they have the same characters and the same bag of frequencies (regardless of which character has which frequency).

## 3. Why This Algorithm Fits

- O(n) time — building two Counters is linear; sorting at most 26 values is O(1).
- O(1) space — at most 26 distinct lowercase letters.
- The two conditions map exactly to the two allowed operations: swapping positions (same chars needed) and swapping frequencies (same frequency multiset needed).

## 4. How It Works

Build a Counter for each string. Check that both have the same set of characters (same keys). Then check that the sorted lists of their frequency values are equal — this confirms the same multiset of frequencies exists.

```python
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())
```

`set(c1) == set(c2)` checks that both strings use the same characters. `sorted(c1.values()) == sorted(c2.values())` checks that the frequency distributions have the same shape — you can't create a character that doesn't exist, so both conditions are necessary.
