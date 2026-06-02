# 20. Valid Parentheses

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/valid-parentheses/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

LIFO (Last-In-First-Out) stack matching using a hashmap to map opening brackets to their closing counterparts.

## 2. How to Recognize the Pattern

- **Nested matching elements**: Brackets, HTML tags, or braces that must close in the reverse order of their opening (LIFO behavior).
- **Resolving inside out**: Innermost brackets must be resolved first before their outer wrapping pairs can be matched, which is the signature use case for a stack.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Single pass where each character in the string is pushed to and popped from the stack at most once.
- **$O(N)$ space**: In the worst case (e.g., all opening brackets like `"((((("`), the stack holds all $N$ characters.
- A hashmap mapping opening-to-closing symbols avoids messy if-else checks when matching pairs.

## 4. How It Works

1. Initialize an empty stack `opening_brackets_stack` and a hashmap `opening_brackets_hashmap` mapping opening bracket characters (`(`, `{`, `[`) to their corresponding closing bracket characters.
2. Iterate through each character `bracket` in the input string `s`.
3. If `bracket` is an opening bracket (a key in the map), append it to the stack.
4. If `bracket` is a closing bracket:
   - Check if the stack is empty. If it is, there is no matching opening bracket, so return `False`.
   - Pop the top opening bracket from the stack and verify if its mapped closing bracket matches `bracket`. If it doesn't, return `False`.
5. After the loop, return `True` if the stack is empty (all opening brackets matched), or `False` if some opening brackets remain unmatched.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets_stack = []
        opening_brackets_hashmap = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        for bracket in s:
            if bracket in opening_brackets_hashmap:
                opening_brackets_stack.append(bracket)
            else:
                if not opening_brackets_stack:
                    return False
                
                previous_opening_bracket = opening_brackets_stack.pop()
                if bracket != opening_brackets_hashmap[previous_opening_bracket]:
                    return False
        return not opening_brackets_stack
```

### Dry Run Table
Input: `s = "()[]{}"`

| Step/Index | bracket | Action | stack state | Check: matches expected? |
|---|---|---|---|---|
| *init* | — | — | `[]` | — |
| 0 | `(` | Push | `["("]` | — |
| 1 | `)` | Pop | `[]` | Pop `(`, maps to `)` (Valid) |
| 2 | `[` | Push | `["["]` | — |
| 3 | `]` | Pop | `[]` | Pop `[`, maps to `]` (Valid) |
| 4 | `{` | Push | `["{"]` | — |
| 5 | `}` | Pop | `[]` | Pop `{`, maps to `}` (Valid) |
| *result* | — | Finish | `[]` | Stack is empty (Valid $\to$ `True`) |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of `s`. We traverse the string exactly once. Stack push and pop operations run in $O(1)$ time.
- **Space Complexity**: $O(N)$ auxiliary space for the stack in the worst case (e.g. all opening brackets).
