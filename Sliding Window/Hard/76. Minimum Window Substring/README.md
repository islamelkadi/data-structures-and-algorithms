# 76. Minimum Window Substring

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/minimum-window-substring/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Variable sliding window with two character-frequency hashmaps and a `curr` counter that tracks how many characters of `t` are currently satisfied by the window.

## 2. How to Recognize the Pattern

- **Minimum window in `s` containing all characters of `t`**: Finding the smallest valid contiguous subarray points to a sliding window that shrinks when the window becomes valid.
- **Frequency-based requirements**: The window must match character frequencies of `t`, suggesting frequency hashmaps.
- **Incremental match counting (`curr`)**: Tracks satisfied characters in $O(1)$ time to avoid costly map scans at each step.

## 3. Why This Algorithm Fits

- **$O(|S| + |T|)$ time**: Each character in `s` is added and removed from the window at most once. Building the frequency map of `t` takes $O(|T|)$ time.
- **$O(|S| + |T|)$ space**: Bounded by the number of unique characters in both strings.
- Maintaining `curr` incrementally checks validity in $O(1)$ time instead of iterating through the maps.

## 4. How It Works

We build `t_hashmap` from `t`. As the `right` pointer expands, we increment the frequency in `s_hashmap`. We only increment `curr` when the character's frequency matches or is less than the required frequency in `t_hashmap` (preventing duplicates from inflating the count). 

Once `curr == t_length`, the window is valid. We record the minimum window size and its starting index, then shrink the window by moving `left` forward. When removing a character causes its count in `s_hashmap` to drop below the required frequency in `t_hashmap`, we decrement `curr` and continue expanding `right`.

```python
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if not s or not t or len(s) < len(t):
            return ""
        if s == t:
            return s

        # Initialize variables
        t_length = len(t)
        t_hashmap = Counter(t)
        s_hashmap = defaultdict(int)
        ans = float("inf")
        curr = left = left_boundary = 0

        for right in range(len(s)):
            # Expand window
            # Add EACH character to the hashmap but only increase CURR if s[right] is in t_hashmap
            # this becomes important in the shrinking window component. If you only add to s_hashmap
            # the characters that are in t_hashmap, then when it's trim to decrease the window and
            # you do a s_hashmap[s[left]] where s[left] is from the s string, you are decreasing the
            # count of s_hashmap[s[left]] where s[left] is NOT in t_hashmap to -1. Therefore, even
            # when s_hashmap[s[left]] is not in t_hashmap the condition that decrements curr will
            # always be true as -1 < 0. Therefore; you are incorrectly decrementing the count.
            if s[right] in t_hashmap:
                s_hashmap[s[right]] += 1 
                if s_hashmap[s[right]] <= t_hashmap[s[right]]:
                    curr += 1

            # Shrink window
            while curr == t_length:

                # Update answer if smaller window found
                if right - left + 1 < ans:
                    ans = right - left + 1
                    left_boundary = left

                # Shrink the window
                if s[left] in s_hashmap:
                    s_hashmap[s[left]] -= 1
                    if s_hashmap[s[left]] < t_hashmap[s[left]]:
                        curr -= 1
                left += 1

        return "" if ans == float("inf") else s[left_boundary: left_boundary + ans]
```

The `<=` and `<` comparison asymmetry is critical: `curr` changes only when matching counts transition across the required threshold.

### Dry Run Table
Input: `s = "ADOBECODEBANC"`, `t = "ABC"`, `t_hashmap = {A:1, B:1, C:1}`

| right | s[right] | s_hashmap | curr | valid? | left | window |
|---|---|---|---|---|---|---|
| 0 | A | `{A:1}` | 1 | no | 0 | — |
| 1 | D | `{A:1, D:1}` | 1 | no | 0 | — |
| 2 | O | `{A:1, D:1, O:1}` | 1 | no | 0 | — |
| 3 | B | `{A:1, D:1, O:1, B:1}` | 2 | no | 0 | — |
| 4 | E | `{A:1, D:1, O:1, B:1, E:1}` | 2 | no | 0 | — |
| 5 | C | `{A:1, D:1, O:1, B:1, E:1, C:1}` | 3 | yes $\to$ shrink | 0 | `"ADOBEC"` len=6 |
| shrink | A leaves | `{A:0, D:1, O:1, B:1, E:1, C:1}` | 2 | no | 1 | — |
| 6 | O | `{A:0, D:1, O:2, B:1, E:1, C:1}` | 2 | no | 1 | — |
| 7 | D | `{A:0, D:2, O:2, B:1, E:1, C:1}` | 2 | no | 1 | — |
| 8 | E | `{A:0, D:2, O:2, B:1, E:2, C:1}` | 2 | no | 1 | — |
| 9 | B | `{A:0, D:2, O:2, B:2, E:2, C:1}` | 2 | no | 1 | — |
| 10 | A | `{A:1, D:2, O:2, B:2, E:2, C:1}` | 3 | yes $\to$ shrink | 1 | `"DOBECODEBA"` $\to$ shrink to `"BANC"` len=4 |
| result | | | | | | `"BANC"` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(|S| + |T|)$ where $|S|$ and $|T|$ are the lengths of strings `s` and `t`. Building `t_hashmap` takes $O(|T|)$ time, and the sliding window pointers `left` and `right` traverse the string `s` at most twice.
- **Space Complexity**: $O(|S| + |T|)$ auxiliary space for the frequency hashmaps, bounded by the alphabet size (the unique characters present in `s` and `t`).
