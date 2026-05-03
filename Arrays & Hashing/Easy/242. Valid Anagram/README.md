# 242. Valid Anagram
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/valid-anagram/

## 1. Algorithm Used

Hash Map (Counter) frequency comparison.

## 2. How to Recognize the Pattern

- "Are two strings anagrams?" → same characters, same counts, different order → frequency counting.
- Comparing character-by-character or sorting both strings works, but counting frequencies is the most direct approach.
- Brute force (sorting) is O(n log n). A frequency map does it in O(n).

## 3. Why This Algorithm Fits

- O(n) time — one pass to build each counter, one pass to compare.
- O(1) space — at most 26 lowercase letters, so the map size is bounded.
- Early exit on length mismatch avoids unnecessary work.

## 4. How It Works

First, if the strings differ in length, they can't be anagrams — return False immediately. Then build a frequency count for each string. Walk through one counter and check that every character appears the same number of times in the other. If any count differs, return False. If the loop completes, they're anagrams.

```python
if len(s) != len(t):
    return False
s_hashset = Counter(s)
t_hashset = Counter(t)
for char, val in t_hashset.items():
    if s_hashset[char] != val:
        return False
return True
```

Since both strings are the same length and every character in `t` matches the count in `s`, there's no way `s` has leftover characters — so checking one direction is enough.
