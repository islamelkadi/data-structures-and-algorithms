# 14. Longest Common Prefix

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/longest-common-prefix/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Vertical scanning with set-size check across all strings column by column.

## 2. How to Recognize the Pattern

- **Find common prefix among all strings**: Scan character positions left to right, stopping at the first mismatch.
- **Bounded by the shortest word**: The common prefix can be no longer than the shortest string in the list, so we find the minimum length first.
- **Set reduction for uniqueness**: Collecting the character at index `i` from each string into a set is a clean way to check if all characters are identical (set size will be exactly 1).

## 3. Why This Algorithm Fits

- **$O(S)$ time**: Where $S$ is the total number of characters across all strings. In the worst case, every character is visited once.
- **$O(N)$ space**: To store at most $N$ characters (one per string) in the set during each column evaluation.
- Stopping at the first mismatch prevents processing longer prefixes in other words.

## 4. How It Works

Find the minimum-length word to bound the column scan. For each column index `i`:
1. Collect the character at position `i` from every string into a set.
2. If the set has exactly one element, all strings match at column `i`, and we append the character to our prefix.
3. If the set size is greater than 1, we stop and return the accumulated prefix.

```python
class Solution:
    
    def get_character(self, strs: str, index: int) -> str:
        return strs[index]
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        # Get lens of words in list
        lens = [len(x) for x in strs]
        
        # Get min lens
        min_len = min(lens)
        
        # Get word of min len
        word = strs[lens.index(min_len)]
        
        # Get ith character
        prefix = ""
        for i in range(min_len):
                        
            if len(set([x[i] for x in strs]))==1:
                prefix += word[i]
            else:
                break
                
        return prefix
```

### Dry Run Table
Input: `strs = ["flower", "flow", "flight"]` $\to$ `min_len = 4`

| i | chars at col i | set | size == 1? | prefix |
|---|---|---|---|---|
| 0 | `"f"`, `"f"`, `"f"` | `{"f"}` | yes | `"f"` |
| 1 | `"l"`, `"l"`, `"l"` | `{"l"}` | yes | `"fl"` |
| 2 | `"o"`, `"o"`, `"i"` | `{"o", "i"}` | no $\to$ break | `"fl"` |

Result: `"fl"`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(S)$ where $S$ is the sum of all characters in all strings in `strs`. In the worst case, we compare every character.
- **Space Complexity**: $O(N)$ auxiliary space (where $N$ is the number of strings) to store characters in the set at each index step.
