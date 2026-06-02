# 917. Reverse Only Letters

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/reverse-only-letters/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Two Pointers (converging/opposite directions) with character-type skipping logic.

## 2. How to Recognize the Pattern

- "Reverse the string according to the following rules: All the characters that are not English letters remain in the same position. All the English letters should be reversed."
- Reversing characters at opposite ends (or subparts) is a classic two-pointer opposite-direction pattern.
- The condition that some characters are skipped while others are swapped means we conditionally advance pointers (`left += 1` or `right -= 1`) depending on whether the current character is an English letter.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(N) where N is the length of `s`, since each character is visited at most once by the pointers.
- **Space Complexity**: O(N) because strings are immutable in Python; converting the string to a list of characters takes O(N) auxiliary space.
- A two-pointer approach avoids nested loops or auxiliary string builders for intermediate states, achieving optimal performance.

## 4. How It Works

1. Define a set/string of valid English letters (`english_letters`).
2. Convert the immutable string `s` to a list of characters `s = list(s)` to allow in-place swapping.
3. Initialize `left` to `0` and `right` to `len(s) - 1`.
4. While `left < right`:
   - If `s[left]` is not an English letter, increment `left` and continue.
   - If `s[right]` is not an English letter, decrement `right` and continue.
   - If both are English letters, swap `s[left]` and `s[right]`, then increment `left` and decrement `right`.
5. Join the character list back into a string and return.

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        english_letters_lowercase = "abcdefghijklmnopqrstuvwxyz"
        english_letters_uppercase = english_letters_lowercase.upper()
        english_letters = english_letters_lowercase + english_letters_uppercase

        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            left_is_english = s[left] in english_letters
            right_is_english = s[right] in english_letters

            if not left_is_english:
                left += 1
                continue
            elif not right_is_english:
                right -= 1
                continue
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
```

### Dry Run Table
Input: `s = "ab-cd"`

Initial list state: `['a', 'b', '-', 'c', 'd']`

| left | right | s[left] | s[right] | left_is_english | right_is_english | Action Taken | list state |
|------|-------|---------|----------|-----------------|------------------|--------------|------------|
| 0    | 4     | 'a'     | 'd'      | True            | True             | Swap, `left=1`, `right=3` | `['d', 'b', '-', 'c', 'a']` |
| 1    | 3     | 'b'     | 'c'      | True            | True             | Swap, `left=2`, `right=2` | `['d', 'c', '-', 'b', 'a']` |
| 2    | 2     | Loop terminates (`left < right` is False) | - | - | - | - | - |

Result: `"dc-ba"`
