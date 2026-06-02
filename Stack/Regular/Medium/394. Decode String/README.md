# 394. Decode String

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/decode-string/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Stack-based decoding with pop-and-reconstruct (regular stack).

## 2. How to Recognize the Pattern

- Nested structure with matching brackets → stack.
- Need to process innermost brackets first → LIFO matches this perfectly.
- Similar to valid parentheses, removing stars, asteroid collision — `]` triggers a "resolve" of everything back to the matching `[`.

## 3. Why This Algorithm Fits

- The stack is both storage and workspace. You don't need separate variables to build intermediate results — pop from the stack, transform, push back onto the stack.
- This is the key insight: the expanded result goes back onto the stack, not into a separate variable. The stack already holds the surrounding context. Pushing back means nested brackets resolve naturally — inner results become part of the outer bracket's content.
- Every `]` resolves one layer. The stack handles arbitrary nesting depth for free.

## 4. How It Works

Push every character except `]`. When you hit `]`:
1. Pop characters until `[` to build the inner string.
2. Pop the `[`.
3. Pop digits to build the repeat count.
4. Push `count * inner_string` back onto the stack — not into a separate variable.

At the end, join everything remaining on the stack. That's your answer.

```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        string = ""
        for char in s:
            
            # Decode string
            if char == "]":
                decoded_string = ""
                while stack[-1] != "[":
                    # important to preserve the encoded string char order
                    decoded_string = stack.pop() + decoded_string
                # Remove the "[" from the stack
                stack.pop()

                # Decode number
                decoded_number = ""
                while stack and stack[-1].isdigit():
                    decoded_number = stack.pop() + decoded_number
                decoded_number = 1 if not decoded_number else int(decoded_number)

                # Push back onto the stack so 
                stack.append(string + decoded_number * decoded_string)
            else:
                stack.append(char)
        return "".join(stack)
```

### Dry Run Table
Input: `s = "3[a2[c]]"`

| Step / Index | char | Action | stack state (after step) | Details |
|--------------|------|--------|--------------------------|---------|
| *init*       | —    | —      | `[]`                     | —       |
| 0            | `3`  | Push   | `["3"]`                  | —       |
| 1            | `[`  | Push   | `["3", "["]`             | —       |
| 2            | `a`  | Push   | `["3", "[", "a"]`        | —       |
| 3            | `2`  | Push   | `["3", "[", "a", "2"]`   | —       |
| 4            | `[`  | Push   | `["3", "[", "a", "2", "["]` | —     |
| 5            | `c`  | Push   | `["3", "[", "a", "2", "[", "c"]` | — |
| 6            | `]`  | Decode | `["3", "[", "a", "cc"]`  | Pop `"c"`, pop `"["`, pop `"2"` $\to$ push `2 * "c"` = `"cc"` |
| 7            | `]`  | Decode | `["accaccacc"]`          | Pop `"cc"`, `"a"` $\to$ `"acc"`. Pop `"["`. Pop `"3"` $\to$ push `3 * "acc"` = `"accaccacc"` |
| *result*     | —    | Finish | `["accaccacc"]`          | Join stack $\to$ `"accaccacc"` |

---

## 5. Time & Space Complexity

- **Time Complexity**: O(n × m) where n is the input length and m is the max expanded length. Each character is pushed/popped at most once, but string expansion (`int * string`) can produce large results.
- **Space Complexity**: O(n × m) — the stack holds expanded strings, which can be much larger than the input (e.g., `100[a]` → 100 characters from 5).
