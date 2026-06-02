# 205. Isomorphic Strings

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/isomorphic-strings/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Bidirectional character mapping using two hashmaps to enforce a strict one-to-one correspondence (bijection).

## 2. How to Recognize the Pattern

- **Character mapping & transformation**: "Check if the characters in `s` can be replaced to get `t`" suggests establishing a consistent character-to-character mapping.
- **Strict one-to-one correspondence**: No two characters in `s` can map to the same character in `t` (and vice-versa). Enforcing this injective relationship requires both a forward map and a reverse map.

## 3. Why This Algorithm Fits

- The algorithm performs a single pass over the strings, yielding $O(N)$ time.
- Two separate maps allow $O(1)$ lookup to detect any conflict in either mapping direction.

## 4. How It Works

1. Initialize `s_hashmap` and `t_hashmap`.
2. Iterate through each index `i` of the strings:
   - If `s[i]` is in `s_hashmap` but points to a character other than `t[i]`, return `False`.
   - If `t[i]` is in `t_hashmap` but points to a character other than `s[i]`, return `False`.
   - Otherwise, record the mapping: `s_hashmap[s[i]] = t[i]` and `t_hashmap[t[i]] = s[i]`.
3. If no conflicts are encountered, return `True`.

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Need a mechanism to map each letter to it's counter part
        # Need a mechanism to check if current letter (that's already mapped) has a different counter part
            # If so - return False
        # Need a mechanism to check if an s letter maps to a t letter used by another s letter
        
        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)):
            if s[i] in s_hashmap and s_hashmap[s[i]] != t[i]:
                return False

            elif t[i] in t_hashmap and t_hashmap[t[i]] != s[i]:
                return False

            s_hashmap[s[i]] = t[i]
            t_hashmap[t[i]] = s[i]

        return True
```

### Dry Run Table
Input: `s = "egg"`, `t = "add"`

| i | `s[i]` | `t[i]` | `s_hashmap` conflict? | `t_hashmap` conflict? | action |
|---|---|---|---|---|---|
| 0 | e | a | no | no | `s_hashmap["e"] = "a"`, `t_hashmap["a"] = "e"` |
| 1 | g | d | no | no | `s_hashmap["g"] = "d"`, `t_hashmap["d"] = "g"` |
| 2 | g | d | `s_hashmap["g"] == "d"` (no conflict) | `t_hashmap["d"] == "g"` (no conflict) | ok |
| **Result** | — | — | — | — | Return `True` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of strings `s` and `t`. We iterate through the strings once.
- **Space Complexity**: $O(K)$ auxiliary space where $K$ is the size of the character set (at most 256 for ASCII values). Since $K$ is bounded, the auxiliary space complexity is $O(1)$.
