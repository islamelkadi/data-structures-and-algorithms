## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Stack-based removal of adjacent same-letter pairs with opposite case.

## 2. How to Recognize the Pattern

- Remove pairs of characters that are "bad" based on a relationship between adjacent elements → stack.
- The "bad" condition involves the current character and the most recently kept character → check stack top.
- Removals can cascade (removing a pair may expose a new bad pair) → stack handles this naturally in one pass.

## 3. Why This Algorithm Fits

- O(n) time — each character is pushed and popped at most once.
- O(n) space — the stack holds the characters kept so far.
- The stack top always represents the last unresolved character, making the adjacent comparison O(1).

## 4. How It Works

Iterate through the string. For each character, check if the stack is non-empty, the top differs from the current character (not identical), but they are the same letter in different cases (`stack[-1].lower() == c.lower()`). If so, pop the top (remove the bad pair). Otherwise, push the current character. The remaining stack contents form the "great" string.

```python
stack = []
for c in s:
    if stack and stack[-1] != c and stack[-1].lower() == c.lower():
        stack.pop()
    else:
        stack.append(c)
return ''.join(stack)
```

The two conditions `stack[-1] != c` and `stack[-1].lower() == c.lower()` together identify same-letter opposite-case pairs — identical characters (e.g., `'a'` and `'a'`) are not bad pairs and should not be removed.

Input: `s = "leEeetcode"`

| c | stack top | bad pair? | action | stack |
|---|-----------|-----------|--------|-------|
| l | — | — | push | [l] |
| e | l | no | push | [l,e] |
| E | e | e≠E, e.lower==E.lower → yes | pop | [l] |
| e | l | no | push | [l,e] |
| e | e | e==e (identical) → no | push | [l,e,e] |
| t | e | no | push | [l,e,e,t] |
| c | t | no | push | [l,e,e,t,c] |
| o | c | no | push | [l,e,e,t,c,o] |
| d | o | no | push | [l,e,e,t,c,o,d] |
| e | d | no | push | [l,e,e,t,c,o,d,e] |
| result | | | join | "leetcode" |
