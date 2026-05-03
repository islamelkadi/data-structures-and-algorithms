## 1. Algorithm Used

Stack simulation of backspace processing, then equality comparison.

## 2. How to Recognize the Pattern

- Characters can be "deleted" by a special character (`#`) → simulate the editing process → stack.
- Need to compare two strings after applying the same transformation → process each independently, then compare.
- Order of operations matters and deletions affect prior characters → stack naturally models this.

## 3. Why This Algorithm Fits

- O(n + m) time — one pass through each string.
- O(n + m) space — two stacks holding the processed characters.
- The stack directly models the text editor: push normal characters, pop on backspace.

## 4. How It Works

For each string, iterate character by character. If the character is not `#`, push it onto the stack. If it is `#` and the stack is non-empty, pop the top (simulate a backspace). After processing both strings, compare the resulting stacks — equal stacks mean equal final strings.

```python
def process(string):
    stack = []
    for c in string:
        if c != '#':
            stack.append(c)
        elif stack:
            stack.pop()
    return stack

return process(s) == process(t)
```

The `elif stack` guard handles leading backspaces on an already-empty string without raising an error.
