# 242. Valid Anagram

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/valid-anagram/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Hash Map (frequency counter) using a single `defaultdict` to track and cross-reference character frequencies.

## 2. How to Recognize the Pattern

- **Are two strings anagrams?**: Anagrams contain the exact same characters in the exact same quantities but in a different order. This indicates frequency counting.
- **Symmetric sizes**: If the lengths of strings `s` and `t` are different, they cannot be anagrams, allowing for an immediate `False` exit.

## 3. Why This Algorithm Fits

- Instead of creating two separate maps and comparing them (which requires extra space and comparisons), we build one map for `s` and decrement counts when iterating through `t`.
- Constant alphabet size: Since the inputs consist of lowercase English letters, the hash map size is bounded by at most 26 keys ($O(1)$ auxiliary space).

## 4. How It Works

1. Check if `len(s) != len(t)`. If so, return `False`.
2. Populate `s_hashmap` with character counts from string `s`.
3. Iterate through string `t`:
   - If the character does not exist in `s_hashmap` or its frequency is already 0, return `False`.
   - Otherwise, decrement its count in `s_hashmap`.
4. If the loop completes successfully, return `True`.

```python
from collections import Counter, defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_hashmap = Counter(s)
        # t_hashmap = Counter(t)
        # return s_hashmap == t_hashmap
        # Contruct counter of s

        # Edge case for early return
        # if the lengths of S & T don't
        # match, because that means they
        # aren't anagrams.
        if len(s) != len(t):
            return False

        # Create dict of chars and frequency
        # for S
        s_hashmap = defaultdict(int)
        for char in s:
            s_hashmap[char] += 1

        # Cross reference chars of t and it's
        # frequency with S. If the a char in
        # T is not in S, then they aren't
        # anagrams.
        for char in t:
            if s_hashmap.get(char, 0) == 0:
                return False
            s_hashmap[char] -= 1

        return True
```

### Dry Run Table
Input: `s = "anagram"`, `t = "nagaram"`

| char (t) | `s_hashmap.get(char, 0)` | action / state (after step) |
|---|---|---|
| *init* | — | `s_hashmap = {"a": 3, "n": 1, "g": 1, "r": 1, "m": 1}` |
| "n" | 1 | `s_hashmap["n"]` decremented to 0 |
| "a" | 3 | `s_hashmap["a"]` decremented to 2 |
| "g" | 1 | `s_hashmap["g"]` decremented to 0 |
| "a" | 2 | `s_hashmap["a"]` decremented to 1 |
| "r" | 1 | `s_hashmap["r"]` decremented to 0 |
| "a" | 1 | `s_hashmap["a"]` decremented to 0 |
| "m" | 1 | `s_hashmap["m"]` decremented to 0 |
| **Result**| — | Return `True` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of strings `s` and `t`. We perform one pass to build the map of `s` and one pass to verify elements against `t`.
- **Space Complexity**: $O(1)$ auxiliary space because the character set is bounded (at most 26 lowercase English letters).
