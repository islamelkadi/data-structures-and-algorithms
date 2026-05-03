## 1. Algorithm Used

Stack-based adjacent duplicate elimination with a single pass.

## 2. How to Recognize the Pattern

- "Remove adjacent duplicates" → each removal can expose a new adjacent pair → stack.
- Repeated removal until no adjacent duplicates remain → stack collapses pairs as you go, no re-scanning needed.
- The result is built left-to-right with the stack contents at the end.

## 3. Why This Algorithm Fits

- O(n) time — each character is pushed and popped at most once.
- O(n) space — the stack holds the result in progress.
- A stack naturally tracks the "last seen" character, making the adjacent comparison O(1).

## 4. How It Works

Iterate through the string. For each character, check if the top of the stack matches it. If it does, pop (remove the pair). If it doesn't, push the character. After the full pass, join the stack into the result string — all adjacent duplicates have been collapsed.

```python
stack = []
for c in s:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)
return ''.join(stack)
```

This handles cascading removals automatically: once a pair is popped, the new top of the stack is compared against the next character without any extra logic.
