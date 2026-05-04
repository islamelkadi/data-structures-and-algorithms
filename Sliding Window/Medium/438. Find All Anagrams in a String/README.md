# 438. Find All Anagrams in a String
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/find-all-anagrams-in-a-string/

## 1. Algorithm Used

Variable-size sliding window with frequency map comparison.

## 2. How to Recognize the Pattern

- "Find all starting indices where a substring is an anagram of p" → fixed-length window (len(p)) with frequency tracking.
- Anagram = same characters, same counts → compare frequency maps.
- Need every valid position, not just one → collect all windows where `s_hashmap == p_hashmap`.

## 3. Why This Algorithm Fits

- O(n) time — each character is added once and removed at most once.
- O(k) space — both hashmaps hold at most k distinct characters where k ≤ 26.
- Shrinking on invalid/over-counted characters keeps the window clean without a separate fixed-size check.

## 4. How It Works

Build a frequency map for `p`. Expand the window by adding `s[right]`. If the current character is either not in `p` or appears more times than allowed, shrink from the left until the count is back in bounds. After shrinking, if the two maps are equal the window is a valid anagram — record `left`.

```python
def shrink_left():
    s_hashmap[s[left]] -= 1
    if not s_hashmap[s[left]]:
        del s_hashmap[s[left]]

for right in range(len(s)):
    s_hashmap[s[right]] += 1

    while s_hashmap[s[right]] > p_hashmap.get(s[right], 0):
        shrink_left()
        left += 1

    if s_hashmap == p_hashmap:
        indices.append(left)
```

The unified `while` condition covers both invalid characters (not in `p`, so `p_hashmap.get` returns 0) and over-counted ones — no need for two separate shrink loops. `shrink_left()` extracts the repeated decrement-and-delete logic to keep the loop body clean.
