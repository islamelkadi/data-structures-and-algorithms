# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Variable-size sliding window using a hash map (`defaultdict`) to track character frequencies in the current window.

## 2. How to Recognize the Pattern

- **"Longest substring without repeating characters"**: Indicates a contiguous subsegment (substring) search under a uniqueness constraint.
- **"No repeating characters"**: Requires tracking character frequencies or presence in the current window.
- **Dynamic window size**: The window expands by moving the `right` pointer and contracts by moving the `left` pointer when a duplicate is detected.

## 3. Why This Algorithm Fits

- **$O(N)$ Time**: Both pointers move from left to right monotonically, visiting each character at most twice.
- **Dynamic Cleanup**: A hash map allows us to either decrement counts or delete characters dynamically as we contract the left boundary, ensuring the window always contains only unique characters.
- **$O(1)$ Hash Map Lookups**: Checking frequency and existence of characters is done in constant time.

## 4. How It Works

1. Initialize `left = 0`, `ans = 0`, and a `defaultdict(int)` named `curr`.
2. Iterate `right` from `0` to `len(s) - 1`:
   - Increment `curr[s[right]]` by 1.
   - While `curr[s[right]] > 1` (meaning the character at `right` is a duplicate):
     - If the character at `left` is unique (`curr[s[left]] == 1`) and is not `s[right]`, delete it from `curr` to save space.
     - If the character at `left` is the duplicate (`curr[s[left]] > 1`), decrement its count.
     - Advance `left` by 1.
   - Update `ans` with the maximum window length found so far (`right - left + 1`).
3. Return `ans`.

```python
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        curr = defaultdict(int)
        for right in range(len(s)):
            curr[s[right]] += 1
            while curr[s[right]] > 1:
                if curr[s[left]] == 1 and s[left] != s[right]:
                    del curr[s[left]]
                
                if curr[s[left]] > 1 and s[left] == s[right]:
                    curr[s[left]] -= 1

                left += 1
            length_curr = sum(curr.values())
            ans = max(ans, right - left + 1)
        return ans
```

### Dry Run Table
Input: `s = "abcabcbb"`

| right | s[right] | curr (before loop) | curr (after loop) | left (after loop) | length_curr | ans |
|---|---|---|---|---|---|---|
| 0 | a | `{'a': 1}` | `{'a': 1}` | 0 | 1 | 1 |
| 1 | b | `{'a': 1, 'b': 1}` | `{'a': 1, 'b': 1}` | 0 | 2 | 2 |
| 2 | c | `{'a': 1, 'b': 1, 'c': 1}` | `{'a': 1, 'b': 1, 'c': 1}` | 0 | 3 | 3 |
| 3 | a | `{'a': 2, 'b': 1, 'c': 1}` | `{'a': 1, 'b': 1, 'c': 1}` | 1 | 3 | 3 |
| 4 | b | `{'a': 1, 'b': 2, 'c': 1}` | `{'a': 1, 'b': 1, 'c': 1}` | 2 | 3 | 3 |
| 5 | c | `{'a': 1, 'b': 1, 'c': 2}` | `{'a': 1, 'b': 1, 'c': 1}` | 3 | 3 | 3 |
| 6 | b | `{'a': 1, 'b': 2, 'c': 1}` | `{'b': 1, 'c': 1}` | 5 | 2 | 3 |
| 7 | b | `{'b': 2, 'c': 1}` | `{'b': 1}` | 7 | 1 | 3 |

Result: `3`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of string `s`. The `right` pointer iterates through the string once, and the `left` pointer can advance at most $N$ times total across the entire execution. Thus, each character is processed at most twice.
- **Space Complexity**: $O(\min(N, M))$ where $M$ is the size of the character alphabet (e.g., 26 for lowercase English letters, 128 for ASCII). The hash map stores at most one entry per unique character in the current window.
