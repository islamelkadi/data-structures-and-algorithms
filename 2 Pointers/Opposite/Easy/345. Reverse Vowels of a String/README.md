# 345. Reverse Vowels of a String

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/reverse-vowels-of-a-string/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Two-pointer inward traversal with hash set lookup.

## 2. How to Recognize the Pattern

- **Selective element reversal**: Reversing only specific elements (e.g., vowels) while keeping others in place indicates a two-pointer approach from both ends (`left` and `right`).
- **Constant lookup condition**: We need to quickly check if a character is a vowel. A hash set provides $O(1)$ lookups.
- **In-place updates**: Since strings are immutable in Python, we convert the string to a list of characters to perform swaps in-place before joining them back.

## 3. Why This Algorithm Fits

- The two pointers move inward toward each other, meaning we scan the string at most once.
- The vowel set is small and fixed in size (10 characters: `aeiouAEIOU`), so membership checks are $O(1)$ time and $O(1)$ space.

## 4. How It Works

1. Convert the string `s` into a list of characters.
2. Initialize two pointers: `left = 0` and `right = len(s) - 1`.
3. While `left < right`:
   - If `s[left]` is not a vowel, increment `left`.
   - If `s[right]` is not a vowel, decrement `right`.
   - If both are vowels, swap `s[left]` and `s[right]`, then increment `left` and decrement `right`.
4. Return the joined list as a string.

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Create hashset for direct lookup
        vowels = set("aeiouAEIOU")

        # Split string in preparation for 
        # switching as strs are immutable
        # in Python
        s = list(s)

        # Initialize 2 ptrs
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            
            if s[right] not in vowels:
                right -= 1
            
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
```

### Dry Run Table
Input: `s = "hello"`

| left | right | s[left] | s[right] | action |
|------|-------|---------|----------|--------|
| 0    | 4     | h       | o        | `h` not a vowel → `left++` |
| 1    | 4     | e       | o        | Both vowels → swap → `"holle"`, move both pointers |
| 2    | 3     | l       | l        | `l` not a vowel → `left++`; `l` not a vowel → `right--` |
| 3    | 2     | —       | —        | `left >= right` → stop |
| result |     |         |          | `"holle"` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of string `s`. Each character is visited at most once as the pointers move toward the middle.
- **Space Complexity**: $O(N)$ auxiliary space to store the characters in a list since Python strings are immutable. The vowel hash set occupies $O(1)$ space.
