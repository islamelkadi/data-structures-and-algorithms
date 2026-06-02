# 340. Longest Substring with At Most K Distinct Characters

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Variable sliding window with a character-frequency map that shrinks from the left whenever the number of distinct characters exceeds `k`.

## 2. How to Recognize the Pattern

- **At most $K$ distinct characters**: Substrings defined by a limit on the number of unique elements point to a variable sliding window with a frequency map.
- **Window validity**: The window is valid as long as the number of unique keys in our frequency map is $\le k$.
- **Map cleanup**: Fully deleting keys when their frequency hits 0 is crucial to keep `len(counts)` representing only active unique characters.

## 3. Why This Algorithm Fits

- The window slides from left to right, expanding `right` and only shrinking `left` when the constraint is violated, ensuring $O(N)$ total operations.
- Storing frequencies in a map/dictionary allows us to track both unique keys and counts in $O(1)$ time for each character.

## 4. How It Works

1. Initialize a hash map `counts` to store character frequencies, two pointers `left = 0` and `right`, and `ans = 0`.
2. Expand the window by advancing `right` and adding `s[right]` to `counts`.
3. If the number of distinct characters in `counts` exceeds `k`:
   - Decrement the count of `s[left]` in the map.
   - If the count becomes 0, delete `s[left]` from the map.
   - Increment `left`.
4. Update `ans = max(ans, right - left + 1)`.
5. Return `ans`.

```python
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
```

### Dry Run Table
Input: `s = "eceba"`, `k = 2`

| right | s[right] | counts | distinct | left | ans |
|-------|---------|--------|----------|------|-----|
| 0     | e       | `{"e": 1}` | 1        | 0    | 1   |
| 1     | c       | `{"e": 1, "c": 1}` | 2        | 0    | 2   |
| 2     | e       | `{"e": 2, "c": 1}` | 2        | 0    | 3   |
| 3     | b       | `{"e": 2, "c": 1, "b": 1}` | $3 > 2 \to$ shrink: delete `c`, `left = 2` | 2    | 3   |
| 4     | a       | `{"e": 2, "b": 1, "a": 1}` | $3 > 2 \to$ shrink: `e: 1`, `e: 0` $\to$ delete `e`, `left = 3` | 3    | 3   |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of string `s`. Each character is processed at most twice (once added at `right`, and at most once removed at `left`).
- **Space Complexity**: $O(K)$ auxiliary space since the frequency map `counts` contains at most $K + 1$ keys at any given time.
