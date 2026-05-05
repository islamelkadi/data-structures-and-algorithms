## 1. Algorithm Used

Sliding window with two frequency hashmaps.

## 2. How to Recognize the Pattern

- "Find all substrings that are anagrams of p" → fixed-concept window (same character set as p).
- Anagram = same characters, same counts → hashmap comparison.
- Shrink from the left whenever a character is invalid or over-counted.

## 3. Why This Algorithm Fits

- O(n) time — each character is added once and removed at most once.
- Shrinking only when a character is over-counted keeps the window as large as possible.
- Comparing two hashmaps is O(1) since the alphabet is fixed size (26 letters).

## 4. How It Works

Maintain `p_hashmap` (fixed) and `s_hashmap` (sliding window). Expand `right` each iteration. If `s[right]` is over-counted relative to `p_hashmap`, shrink from `left` until it's valid. When both maps are equal, the window is an anagram — record `left`.

```python
for right in range(len(s)):
    s_hashmap[s[right]] += 1

    while s_hashmap[s[right]] > p_hashmap.get(s[right], 0):
        shrink_left()
        left += 1

    if s_hashmap == p_hashmap:
        indices.append(left)
```

Example with `s = "cbaebabacd"`, `p = "abc"`:
- right=2: window "cba" == p_hashmap → append 0
- right=6: window "bac" == p_hashmap → append 6
- Result: `[0, 6]`

## 5. Time & Space Complexity

Time: O(n) — each character enters and leaves the window at most once.

Space: O(1) — hashmaps are bounded by alphabet size (26).
