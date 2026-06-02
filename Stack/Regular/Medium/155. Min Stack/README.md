# 155. Min Stack

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/min-stack/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Auxiliary state tracking using dual stacks. We maintain a primary stack to store data values and a parallel `min_stack` to track the running minimum value corresponding to each layer of the main stack.

## 2. How to Recognize the Pattern

- **O(1) state property lookups**: Designing a custom stack class where we need to query historical properties (such as the minimum element) in $O(1)$ time.
- **Historical state tracking**: Storing the "minimum so far" at each level of the stack enables us to retrieve the correct minimum in $O(1)$ even after popping elements.

## 3. Why This Algorithm Fits

- Both lists are synchronized in size: push and pop operations happen in tandem.
- Since stack indexing and append/pop operations are $O(1)$ time, all methods (`push`, `pop`, `top`, `getMin`) achieve constant $O(1)$ time complexity.

## 4. How It Works

1. Initialize two lists: `self.stack` (stores all elements) and `self.min_stack` (stores the running minimums).
2. **`push(val)`**:
   - Append `val` to `self.stack`.
   - Calculate the new running minimum: `min_val = min(val, self.min_stack[-1] if self.min_stack else val)`.
   - Append `min_val` to `self.min_stack`.
3. **`pop()`**:
   - Pop the top element from both `self.stack` and `self.min_stack`.
4. **`top()`**:
   - Return the last element of `self.stack` (`self.stack[-1]`).
5. **`getMin()`**:
   - Return the last element of `self.min_stack` (`self.min_stack[-1]`).

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
```

### Dry Run Table
Trace of Operations: `push(2)`, `push(3)`, `getMin()`, `push(1)`, `getMin()`, `pop()`, `getMin()`

| Step | Operation | val | stack state | min_stack state | Output / Return Value |
|------|-----------|-----|-------------|-----------------|-----------------------|
| init | —         | —   | `[]`        | `[]`            | —                     |
| 1    | push(2)   | 2   | `[2]`       | `[2]`           | —                     |
| 2    | push(3)   | 3   | `[2, 3]`    | `[2, 2]`        | —                     |
| 3    | getMin()  | —   | `[2, 3]`    | `[2, 2]`        | 2                     |
| 4    | push(1)   | 1   | `[2, 3, 1]` | `[2, 2, 1]`     | —                     |
| 5    | getMin()  | —   | `[2, 3, 1]` | `[2, 2, 1]`     | 1                     |
| 6    | pop()     | —   | `[2, 3]`    | `[2, 2]`        | —                     |
| 7    | getMin()  | —   | `[2, 3]`    | `[2, 2]`        | 2                     |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(1)$ for all operations (`push`, `pop`, `top`, `getMin`).
- **Space Complexity**: $O(N)$ auxiliary space where $N$ is the number of elements in the stack. We store one running minimum value for each element pushed.
