# 242. Valid Anagram
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/valid-anagram/

## 1. Algorithm Used

Frequency map comparison using `Counter` on both strings.

## 2. How to Recognize the Pattern

- "same characters, possibly different order" → compare character frequencies → Counter.
- Strings of different lengths can never be anagrams → early exit on length mismatch.
- Equality of two Counters is a direct O(k) check where k is the alphabet size.

## 3. Why This Algorithm Fits

- O(n) time — building each Counter is a single pass; comparing them is O(k) where k ≤ 26 for lowercase letters.
- O(k) space — each Counter holds at most k distinct characters.
- Counter comparison is cleaner and less error-prone than manually tracking differences.

## 4. How It Works

After an early-exit length check, build a `Counter` for each string. Then iterate over the characters in one Counter and verify that the count for each character matches in the other. Any mismatch returns False; completing the loop returns True.

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

The length check is a cheap guard that eliminates the most obvious non-anagram case before any counting work is done.
