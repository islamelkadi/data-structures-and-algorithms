# 438. Find All Anagrams in a String

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/find-all-anagrams-in-a-string/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Sliding window with two frequency hashmaps.

## 2. How to Recognize the Pattern

- "Find all substrings that are anagrams of p" → fixed-concept window (same character set as p).
- Anagram = same characters, same counts → hashmap comparison.
- Shrink from the left whenever a character is invalid (not in target) or over-counted (exceeds target requirement).

## 3. Why This Algorithm Fits

- **Time Complexity**: O(n) — each character enters and leaves the window at most once.
- **Space Complexity**: O(1) — the hashmaps are bounded by the alphabet size (at most 26 letters).
- Comparing two hashmaps is O(1) since the maximum number of unique characters is 26.

## 4. How It Works

Maintain `p_hashmap` (fixed target frequencies) and `s_hashmap` (sliding window frequencies). Expand `right` each iteration.
1. If `s[right]` is not in `p_hashmap`, shrink from the left to discard all elements in the current window up to `right`.
2. If `s[right]` is in `p_hashmap` but its count exceeds the required target frequency, shrink from `left` until the excess count is removed.
3. Compare both maps; if they match, the window is an anagram, so record `left`.

```python
from collections import Counter, defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        indices = []
        left = 0
        p_hashmap = Counter(p)
        s_hashmap = defaultdict(int)
        for right in range(len(s)):
            # Expand window
            s_hashmap[s[right]] += 1

            while s_hashmap and s[right] not in p_hashmap:
                s_hashmap[s[left]] -= 1
                if not s_hashmap[s[left]]:
                    del s_hashmap[s[left]]
                left += 1

            while s[right] in p_hashmap and s_hashmap[s[right]] > p_hashmap[s[right]]:
                s_hashmap[s[left]] -= 1
                if not s_hashmap[s[left]]:
                    del s_hashmap[s[left]]
                left += 1

            if s_hashmap == p_hashmap:
                indices.append(left)
                
        return indices
```

### Dry Run Table
Input: `s = "cbaebabacd"`, `p = "abc"`, `p_hashmap = {'a':1, 'b':1, 'c':1}`

| right | s[right] | s_hashmap | Shrink condition met? | left | == p_hashmap? | indices |
|-------|---------|-----------|------------------------|------|---------------|---------|
| 0     | c       | `{c:1}`   | no                     | 0    | no            | `[]`    |
| 1     | b       | `{c:1, b:1}` | no                  | 0    | no            | `[]`    |
| 2     | a       | `{c:1, b:1, a:1}` | no               | 0    | yes           | `[0]`   |
| 3     | e       | `{c:1, b:1, a:1, e:1}` | yes (`'e'` not in p) $\to$ shrink c,b,a | 4 | no | `[0]` |
| 4     | b       | `{b:1}`   | no                     | 4    | no            | `[0]`   |
| 5     | a       | `{b:1, a:1}` | no                  | 4    | no            | `[0]`   |
| 6     | b       | `{b:2, a:1}` | yes (b count > 1) $\to$ shrink b | 5 | no      | `[0]`   |
| 7     | a       | `{b:1, a:2}` | yes (a count > 1) $\to$ shrink a | 6 | no      | `[0]`   |
| 8     | c       | `{b:1, a:1, c:1}` | no               | 6    | yes           | `[0, 6]`|
| 9     | d       | `{b:1, a:1, c:1, d:1}` | yes (`'d'` not in p) $\to$ shrink b,a,c | 10 | no | `[0, 6]`|

---

## 5. Time & Space Complexity

- **Time Complexity**: O(n) — each character enters and leaves the window at most once.
- **Space Complexity**: O(1) — hashmaps are bounded by the alphabet size (26).
