# 424. Longest Repeating Character Replacement

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/longest-repeating-character-replacement/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Variable-size sliding window with frequency map. We expand the window with a `right` pointer and count character frequencies in the current window. If the number of characters that need to be replaced exceeds `k`, we shrink the window from the `left`.

## 2. How to Recognize the Pattern

- Looking for the longest contiguous substring (sliding window) under a constraint where we can flip/change at most `k` characters.
- In any window, the number of replacements needed to make all characters equal is the window size minus the frequency of the most frequent character: `(right - left + 1) - max_freq`.
- As the window grows, the replacement count is monotonic; if we exceed `k`, we must shrink `left` to restore validity.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(n) — single pass where the inner shrink loop only runs at most `n` times total (O(N) amortized). Fetching `max(window.values())` takes O(26) = O(1) time because the alphabet size is bounded.
- **Space Complexity**: O(1) — the hash map only stores counts for at most 26 unique English letters.

## 4. How It Works

1. Initialize `left = ans = 0` and `window` as a frequency map.
2. Iterate `right` through the string, incrementing the count of `s[right]`.
3. Compute `curr` = number of replacements needed = `(right - left + 1) - max(window.values())`.
4. If `curr > k`, decrement the frequency of `s[left]` in the map, increment `left`, and decrement `curr` by 1 (since reducing the window size by 1 reduces the required replacements by at most 1).
5. Track the maximum valid window size using `ans = max(ans, right - left + 1)`.

```python
# The question wants you to find the longest substring containing the
# same letter that can be flipped. You need to examine the number of
# chars that can be flipped in the LOCAL window as opposed to the
# entire string.
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = ans = 0
        window = defaultdict(int)

        for right in range(len(s)): # O(n)
            # Add new character to window
            window[s[right]] = window.get(s[right], 0) + 1
            
            # curr = number of chars we need to replace
            # window length - count of most frequent char
            curr = (right - left + 1) - max(window.values()) # O(26)-> 0(1)

            # If we need more replacements than k allows
            while curr > k: # O(N) amortized
                window[s[left]] -= 1
                left += 1
                curr -= 1  # Simply decrement by 1 since window size reduced by 1
                
            ans = max(ans, right - left + 1)
            
        return ans
```

### Dry Run Table
Input: `s = "AABABBA"`, `k = 1`

| Step/right | s[right] | window state | max(freq) | window size | curr (replacements) | Action (if curr > k) | left | ans |
|------------|----------|--------------|-----------|-------------|---------------------|----------------------|------|-----|
| init       | —        | {}           | 0         | 0           | 0                   | —                    | 0    | 0   |
| 0          | A        | {A:1}        | 1         | 1           | 1 - 1 = 0           | —                    | 0    | 1   |
| 1          | A        | {A:2}        | 2         | 2           | 2 - 2 = 0           | —                    | 0    | 2   |
| 2          | B        | {A:2, B:1}   | 2         | 3           | 3 - 2 = 1           | —                    | 0    | 3   |
| 3          | A        | {A:3, B:1}   | 3         | 4           | 4 - 3 = 1           | —                    | 0    | 4   |
| 4          | B        | {A:3, B:2}   | 3         | 5           | 5 - 3 = 2           | curr > 1 → A count to 2, left=1, curr=1 | 1 | 4   |
| 5          | B        | {A:2, B:3}   | 3         | 5           | 5 - 3 = 2           | curr > 1 → A count to 1, left=2, curr=1 | 2 | 4   |
| 6          | A        | {A:2, B:3}   | 3         | 5           | 5 - 3 = 2           | curr > 1 → B count to 2, left=3, curr=1 | 3 | 4   |

---

## 5. Time & Space Complexity

- **Time Complexity**: O(n) — single pass where the inner shrink loop only runs at most `n` times total (O(N) amortized). Fetching `max(window.values())` takes O(26) = O(1) time because the alphabet size is bounded.
- **Space Complexity**: O(1) — the hash map only stores counts for at most 26 unique English letters.
