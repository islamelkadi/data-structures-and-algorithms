# 1189. Maximum Number of Balloons

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/maximum-number-of-balloons/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Alternative Solution (O(1) Space)](#5-alternative-solution-o1-space)

## 1. Algorithm Used

HashMap / Frequency Counting using a Counter to count the frequency of characters in `text` that form the word `"balloon"`.

## 2. How to Recognize the Pattern

- "form as many instances of the word 'balloon' as possible" → matching count/frequency of key characters (`b`, `a`, `l`, `o`, `n`).
- The characters can be in any order, which is a classic hashing/frequency map signal.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(N) where N is the length of `text` since we loop through `text` once to build the frequency map.
- **Space Complexity**: O(1) (or O(N) conceptually) because our map size is bounded by the number of unique characters in the word `"balloon"` (which is 5 distinct characters: `b`, `a`, `l`, `o`, `n`).
- It allows us to calculate how many instances we can form by looking at the bottleneck character frequency (divided by its requirement in `"balloon"`).

## 4. How It Works

1. Build a target frequency map for `"balloon"`: `{'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}`.
2. Build a frequency count of only these target characters present in `text`.
3. If any of the required characters are missing, return `0`.
4. Divide the count of each character in `text` by its count in the target word `"balloon"` (e.g., `l` and `o` are divided by 2).
5. The maximum number of words we can form is limited by the minimum value of these quotients.

```python
from collections import Counter, defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_hashmap = defaultdict(int)
        balloon_hashset = Counter("balloon")
        
        for char in text:
            if char in balloon_hashset:
                text_hashmap[char] += 1

        if len(text_hashmap) != len(balloon_hashset):
            return 0
        
        for key, val in text_hashmap.items():
            text_hashmap[key] = val // balloon_hashset[key]
        
        return min(text_hashmap.values())
```

### Dry Run Table
Input: `text = "loonbalxballpoon"`, `balloon_hashset = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}`

- **First Pass (Building `text_hashmap`):**
  - Character frequencies in `text` for `"balloon"` characters: `{'l': 4, 'o': 4, 'n': 2, 'b': 2, 'a': 2}`.

- **Second Pass (Dividing by target frequency):**

| Key | val (in text) | balloon_hashset[key] | val // target | text_hashmap[key] after division |
|-----|---------------|----------------------|---------------|----------------------------------|
| *init* | - | - | - | `{'l': 4, 'o': 4, 'n': 2, 'b': 2, 'a': 2}` |
| `l` | 4 | 2 | `4 // 2 = 2` | `{'l': 2, ...}` |
| `o` | 4 | 2 | `4 // 2 = 2` | `{'l': 2, 'o': 2, ...}` |
| `n` | 2 | 1 | `2 // 1 = 2` | `{'l': 2, 'o': 2, 'n': 2, ...}` |
| `b` | 2 | 1 | `2 // 1 = 2` | `{'l': 2, 'o': 2, 'n': 2, 'b': 2, ...}` |
| `a` | 2 | 1 | `2 // 1 = 2` | `{'l': 2, 'o': 2, 'n': 2, 'b': 2, 'a': 2}` |

- **Minimum value in map**: `min(2, 2, 2, 2, 2) = 2`.
- **Result**: `2`.

---

## 5. Alternative Solution (O(1) Space)

A more elegant solution counting character occurrences directly:
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a = text.count('a')
        l = text.count('l') // 2
        o = text.count('o') // 2
        n = text.count('n')
        return min(b, a, l, o, n)
```
- **Time Complexity**: O(N) as it scans the string a few times.
- **Space Complexity**: O(1) as it uses 5 integer variables.
