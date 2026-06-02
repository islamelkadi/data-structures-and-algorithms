# 71. Simplify Path

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/simplify-path/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Stack-based Unix path simplification by processing split components.

## 2. How to Recognize the Pattern

- **Unix path normalization with `.`, `..`, and multiple slashes**: Stack is the natural data structure to track directory levels.
- `..` means "go up one level" $\to$ pop from the stack.
- `.` means "stay in current directory" and empty string (caused by double slashes `//`) $\to$ skip/ignore.
- The result is built as a single absolute path from the stack contents.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Splitting the path and iterating over the components takes linear time.
- **$O(N)$ space**: The stack holds at most $N/2$ directory names.
- A stack directly models directory hierarchy: pushing when descending, popping when ascending.

## 4. How It Works

Split the path on `/` to get individual components. For each component:
1. If it is `.` or an empty string, continue.
2. If it is not `..`, we append it to the stack.
3. If it is `..`, we pop from the stack (if the stack is not empty).
4. Reconstruct the result by joining the stack with `/` and prepending a leading `/`.

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        # splitting by a `/` delimeter will resolve multiple back to back slashes
        stack = []
        for dir_ in path.split("/") :
            # If dir_ is current `'.'` or empty string because of the delimeter split then continue
            if dir_ == "." or dir_ == "":
                continue
            if dir_ != "..":
                stack.append(dir_)
            elif stack:
                stack.pop()
        return "/" + "/".join(stack)
```

The guard `elif stack` on the `..` case handles paths like `/../` that attempt to navigate above the root directory; they remain at the root rather than causing an error.

### Dry Run Table
Input: `path = "/home//foo/"`

| part | action | stack |
|---|---|---|
| `""` | empty $\to$ skip | `[]` |
| `"home"` | push | `["home"]` |
| `""` | empty $\to$ skip | `["home"]` |
| `"foo"` | push | `["home", "foo"]` |
| `""` | empty $\to$ skip | `["home", "foo"]` |
| result | `"/" + join` | `"/home/foo"` |

Result: `"/home/foo"`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of `path`. Splitting the path takes $O(N)$ time. Each stack push and pop operation takes $O(1)$ time, and joining the stack at the end takes $O(N)$ time.
- **Space Complexity**: $O(N)$ to store the path components in the split list and the stack.
