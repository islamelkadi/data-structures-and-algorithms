# 1047. Remove All Adjacent Duplicates In String

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Stack-based adjacent duplicate elimination with a single pass.

## 2. How to Recognize the Pattern

- "Remove adjacent duplicates" → each removal can expose a new adjacent pair → stack.
- Repeated removal until no adjacent duplicates remain → stack collapses pairs as you go, no re-scanning needed.
- The result is built left-to-right with the stack contents at the end.

## 3. Why This Algorithm Fits

- **Time Complexity**: O(n) — each character is pushed and popped at most once.
- **Space Complexity**: O(n) — the stack holds the result in progress.
- A stack naturally tracks the "last seen" character, making the adjacent comparison O(1).

## 4. How It Works

Iterate through the string. For each character, check if the top of the stack matches it. If it does, pop (remove the pair). If it doesn't, push the character. After the full pass, join the stack into the result string — all adjacent duplicates have been collapsed.

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
```

This handles cascading removals automatically: once a pair is popped, the new top of the stack is compared against the next character without any extra logic.

### Dry Run Table
Input: `s = "abbaca"`

| char | stack top | Condition: `stack and char == stack[-1]` | Action Taken | stack |
|------|-----------|------------------------------------------|--------------|-------|
| a    | —         | Empty stack → False                      | Push 'a'     | `['a']` |
| b    | 'a'       | `'b' == 'a'` → False                     | Push 'b'     | `['a', 'b']` |
| b    | 'b'       | `'b' == 'b'` → True                      | Pop 'b'      | `['a']` |
| a    | 'a'       | `'a' == 'a'` → True                      | Pop 'a'      | `[]` |
| c    | —         | Empty stack → False                      | Push 'c'     | `['c']` |
| a    | 'c'       | `'a' == 'c'` → False                     | Push 'a'     | `['c', 'a']` |

**Result**: `"ca"` (joined stack)
