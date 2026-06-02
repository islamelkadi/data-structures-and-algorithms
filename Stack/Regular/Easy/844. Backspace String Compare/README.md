# 844. Backspace String Compare

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/backspace-string-compare/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Stack simulation of backspace processing, followed by equality comparison of the resulting stacks.

## 2. How to Recognize the Pattern

- Characters can be "deleted" by a special character (`#`) → simulate the editing process → stack.
- Need to compare two strings after applying the same transformation → process each independently, then compare.
- Order of operations matters and deletions affect prior characters → stack naturally models this (LIFO).

## 3. Why This Algorithm Fits

- **Time Complexity**: O(n + m) — one pass through each string where n and m are their lengths.
- **Space Complexity**: O(n + m) — two stacks holding the processed characters.
- The stack directly models the text editor: push normal characters, pop on backspace.

## 4. How It Works

For each string, iterate character by character. If the character is not `#`, push it onto the stack. If it is `#` and the stack is non-empty, pop the top (simulate a backspace). After processing both strings, compare the resulting stacks — equal stacks mean equal final strings.

```python
class Solution:
    def delete_char(self, string: str):
        stack = []
        for char in string:
            if char != "#":
                stack.append(char)
            elif char == "#" and stack:
                stack.pop()
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:  
        return self.delete_char(s) == self.delete_char(t)
```

The `elif char == "#" and stack` condition handles leading/extra backspaces on an already-empty string safely by doing nothing.

### Dry Run Table
Input: `s = "ab#c"`, `t = "ad#c"`

**Process `s = "ab#c"`:**

| char | action | stack |
|------|--------|-------|
| a    | push   | `['a']` |
| b    | push   | `['a', 'b']` |
| #    | pop    | `['a']` |
| c    | push   | `['a', 'c']` |

**Process `t = "ad#c"`:**

| char | action | stack |
|------|--------|-------|
| a    | push   | `['a']` |
| d    | push   | `['a', 'd']` |
| #    | pop    | `['a']` |
| c    | push   | `['a', 'c']` |

Result: `delete_char("ab#c") == delete_char("ad#c")` $\to$ `['a', 'c'] == ['a', 'c']` $\to$ `True`
