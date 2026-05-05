## 1. Algorithm Used

Stack-based Unix path simplification by processing split components.

## 2. How to Recognize the Pattern

- Path with `.`, `..`, and multiple slashes → normalize it → stack to track directory levels.
- `..` means "go up one level" → pop from stack; `.` means "stay" → skip; empty string from `//` → skip.
- The result is always an absolute path built from the stack contents.

## 3. Why This Algorithm Fits

- O(n) time — splitting and iterating over path components is linear.
- O(n) space — the stack holds at most n/2 directory names.
- A stack directly models the directory hierarchy: push when descending, pop when ascending.

## 4. How It Works

Split the path on `/` to get individual components. For each component: if it's `..` and the stack is non-empty, pop (go up one directory); if it's non-empty and not `.`, push it (enter a directory). Empty components (from consecutive slashes) and `.` are simply skipped. Reconstruct the result by joining the stack with `/` and prepending a leading `/`.

```python
stack = []
for part in path.split('/'):
    if part == '..':
        if stack:
            stack.pop()
    elif part and part != '.':
        stack.append(part)
return '/' + '/'.join(stack)
```

The guard `if stack` on the `..` case handles paths like `/../` that try to go above root — they stay at root rather than causing an error.

Input: `path = "/home//foo/"`

| part | action | stack |
|------|--------|-------|
| "" | empty → skip | [] |
| "home" | push | ["home"] |
| "" | empty → skip | ["home"] |
| "foo" | push | ["home","foo"] |
| "" | empty → skip | ["home","foo"] |
| result | "/" + join | "/home/foo" |
