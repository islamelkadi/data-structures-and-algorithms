## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Stack-based character removal where `*` deletes the most recent non-star character.

## 2. How to Recognize the Pattern

- A special character removes the "closest" preceding character → stack (LIFO order matches "closest preceding").
- The problem guarantees a valid operation sequence → no need to guard against popping an empty stack.
- Build the result from what remains after all deletions → join the stack at the end.

## 3. Why This Algorithm Fits

- O(n) time — each character is pushed or popped exactly once.
- O(n) space — the stack holds the surviving characters.
- The stack top always points to the most recently added character, making deletion O(1).

## 4. How It Works

Iterate through the string. If the current character is `*`, pop the top of the stack (remove the closest non-star character to the left). Otherwise, push the character. After the full pass, join the stack to form the result.

```python
stack = []
for c in s:
    if c == '*':
        stack.pop()
    else:
        stack.append(c)
return ''.join(stack)
```

The problem guarantees every `*` has a character to delete, so no empty-stack guard is needed — this keeps the logic minimal.

Input: `s = "leet**cod*e"`

| c | action | stack |
|---|--------|-------|
| l | push | [l] |
| e | push | [l,e] |
| e | push | [l,e,e] |
| t | push | [l,e,e,t] |
| * | pop | [l,e,e] |
| * | pop | [l,e] |
| c | push | [l,e,c] |
| o | push | [l,e,c,o] |
| d | push | [l,e,c,o,d] |
| * | pop | [l,e,c,o] |
| e | push | [l,e,c,o,e] |
| result | join | "lecoe" |
