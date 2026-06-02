# 1657. Determine if Two Strings Are Close
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/determine-if-two-strings-are-close/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Notes & Lessons Learned](#5-notes--lessons-learned)

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

Input: `word1 = "abc"`, `word2 = "bca"`

| step | c1 | c2 | set(c1)==set(c2)? | sorted values match? | result |
|------|----|----|-------------------|----------------------|--------|
| build | {a:1,b:1,c:1} | {b:1,c:1,a:1} | {a,b,c}=={a,b,c} ✓ | [1,1,1]==[1,1,1] ✓ | True |

## 5. Notes & Lessons Learned

> [!NOTE]
> **Avoid Re-creating the Transformation/Reordering Algorithm**:
> Do not attempt to simulate the reordering or swapping algorithm to transform `word1` into `word2`. 
>
> The problem only asks to confirm **if it is possible** to do so. We can verify this via structural comparison of the frequencies:
> 1. Ensure the lengths are equal.
> 2. Ensure both strings contain the exact same set of unique characters (since you cannot introduce new characters).
> 3. Ensure the sorted frequency multisets are identical (meaning the "shape" of frequency distribution is the same, allowing us to swap counts).
