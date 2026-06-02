# 1768. Merge Strings Alternately

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/merge-strings-alternately/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)
5. [Alternative Implementations & Pitfalls](#5-alternative-implementations--pitfalls)

## 1. Algorithm Used

The algorithm utilizes a single-pointer interleaved traversal (Two Arrays/Sequences). A single index is used to walk through both input strings simultaneously, appending characters alternately.

## 2. How to Recognize the Pattern

- **Interleaving / Merging Alternately**: Whenever two arrays or strings need to be combined by alternating elements, we need a sequential traversal of both collections.
- **Synchronized vs. Independent Advancement**: Because both collections advance at the exact same pace (one character per iteration step), a single shared pointer `i` works. Two separate pointers are only necessary if the collections advance at different speeds.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N + M)$ where $N$ and $M$ are the lengths of `word1` and `word2`, respectively. Each character of both strings is visited exactly once.
- **Space Complexity**: $O(N + M)$ to store the resulting merged string.

## 4. How It Works

Use a single index `i` starting at 0. While `i` is smaller than the length of either string:
1. If `i` is in bounds of `word1`, append `word1[i]`.
2. If `i` is in bounds of `word2`, append `word2[i]`.
3. Increment `i` by 1.

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged_str += word1[i]
            if i < len(word2):
                merged_str += word2[i]
            i += 1
        return merged_str
```

### Dry Run Table
Input: `word1 = "ab"`, `word2 = "qrs"`

| Step/Index (`i`) | `i < len(word1)` | Append `word1[i]` | `i < len(word2)` | Append `word2[i]` | `merged_str` | Action Taken |
|------------------|------------------|-------------------|------------------|-------------------|--------------|--------------|
| *init*           | —                | —                 | —                | —                 | `""`         | Initialize `i = 0` |
| 0                | `0 < 2` (True)   | `'a'`             | `0 < 3` (True)   | `'q'`             | `"aq"`       | Append both, `i` $\to$ 1 |
| 1                | `1 < 2` (True)   | `'b'`             | `1 < 3` (True)   | `'r'`             | `"aqbr"`     | Append both, `i` $\to$ 2 |
| 2                | `2 < 2` (False)  | —                 | `2 < 3` (True)   | `'s'`             | `"aqbrs"`    | Append `'s'`, `i` $\to$ 3 |
| 3                | `3 < 2` (False)  | —                 | `3 < 3` (False)  | —                 | `"aqbrs"`    | Terminate loop |

---

## 5. Alternative Implementations & Pitfalls

### Option 1: Two Independent Pointers
We can maintain two separate pointers (`w1`, `w2`) tracking progress in each string:

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        w1, w2 = 0, 0
        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1):
                merged_str += word1[w1]
                w1 += 1
            if w2 < len(word2):
                merged_str += word2[w2]
                w2 += 1
        return merged_str
```

### Option 2: Single-Pointer Double-Increment Bug
A common pitfall when trying to use a single pointer is incrementing `i` inside each conditional block:

```python
# BUGGY CODE
merged_str = ""
i = 0
while not (i >= len(word1) and i >= len(word2)):
    if i < len(word1):
        merged_str += word1[i]
        i += 1  # Increments i
    if i < len(word2):
        merged_str += word2[i]
        i += 1  # Increments i again!
```

> [!WARNING]
> **Why the bug happens**:
> For `word1 = "abc"`, `word2 = "def"`:
> - **At `i = 0`**: `'a'` is appended, `i` becomes `1`. Then `'e'` (at index 1 of `word2`) is appended instead of `'d'` (at index 0 of `word2`), and `i` becomes `2`.
> - **At `i = 2`**: `'c'` is appended, `i` becomes `3`.
> - **Result**: `"aec"` instead of `"adbecf"`.
> 
> **Fix**: Keep pointer increments outside of individual array checks, advancing the index only once per loop iteration.
