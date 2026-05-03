# Stack

## 1. What It Is

A stack is a Last-In-First-Out (LIFO) data structure. In algorithm problems, stacks appear in two distinct roles:

**Regular stack**: tracks a history of elements so you can undo, match, or process them in reverse order. The stack holds "pending" work that gets resolved when a matching or closing event arrives.

**Monotonic stack**: maintains elements in sorted order (increasing or decreasing) to efficiently answer "what is the next greater/smaller element to the right/left?" The stack discards elements that can no longer be the answer for future queries.

These two uses look similar in code but solve fundamentally different problem types.

## 2. When to Use It — Pattern Recognition

### Keywords that signal a regular stack:
- "matching pairs" / "valid parentheses" / "balanced brackets" → push open, pop on close
- "undo" / "backspace" / "delete previous" → push characters, pop on delete signal
- "nested structure" / "decode string" / "evaluate expression" → stack frames for nesting depth
- "simplify path" / "canonical path" → push directories, pop on `..`
- "remove adjacent duplicates" → push and compare top

### Keywords that signal a monotonic stack:
- "next greater element" / "next smaller element" → classic monotonic stack
- "daily temperatures" / "how many days until warmer" → next greater to the right
- "largest rectangle in histogram" → next smaller to the left and right
- "car fleet" / "catch up" problems → monotonic reasoning about ordering
- "stock span" → next greater to the left

### Problem characteristics:
- You need to process elements and refer back to recent history → regular stack
- You need the nearest element satisfying a comparison for every position → monotonic stack
- The problem involves nesting or recursion-like structure → regular stack
- Brute force would scan left or right for each element → monotonic stack (O(n) instead of O(n²))

## 3. Core Technique(s)

### Technique A: Regular Stack — Matching/Nesting

Push when you open; pop and validate when you close.

```python
stack = []
pairs = {')': '(', ']': '[', '}': '{'}

for ch in s:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack or stack[-1] != pairs[ch]:
            return False
        stack.pop()

return len(stack) == 0
```

### Technique B: Regular Stack — Character Processing

Push characters; pop when a condition is met (backspace, adjacent duplicate, etc.).

```python
stack = []
for ch in s:
    if ch == '#':          # backspace
        if stack:
            stack.pop()
    else:
        stack.append(ch)
return ''.join(stack)
```

### Technique C: Monotonic Stack — Next Greater Element

Maintain a decreasing stack. When a larger element arrives, it is the "next greater" for everything it pops.

```python
stack = []   # stores indices
result = [-1] * len(arr)

for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        result[idx] = arr[i]   # arr[i] is the next greater for idx
    stack.append(i)

return result
```

For **next smaller**: flip the comparison to `arr[stack[-1]] > arr[i]`.
For **previous greater/smaller**: iterate right to left, or process the stack differently.

### Technique D: Monotonic Stack — Histogram (Largest Rectangle)

Use a stack to track bars whose rectangles are still "open" (no shorter bar has appeared to their right yet).

```python
stack = []   # (height, start_index)
max_area = 0

for i, h in enumerate(heights):
    start = i
    while stack and stack[-1][0] > h:
        height, start = stack.pop()
        max_area = max(max_area, height * (i - start))
    stack.append((h, start))

for height, start in stack:
    max_area = max(max_area, height * (len(heights) - start))

return max_area
```

## 4. Decision Framework

```
Does the problem involve matching, nesting, or undoing?
└── Regular stack
    ├── Parentheses / brackets → push open, pop on close
    ├── Backspace / delete → push chars, pop on signal
    ├── Nested encoding → push (result, multiplier) on open bracket
    └── Path simplification → push dirs, pop on ".."

Does the problem ask "nearest X to the left/right" for each element?
└── Monotonic stack
    ├── Next greater → decreasing stack, pop when larger arrives
    ├── Next smaller → increasing stack, pop when smaller arrives
    └── Largest rectangle → track open bars, close on shorter bar
```

## 5. One-Pass vs Multi-Pass Reasoning

**Regular stack**: almost always one pass. The stack accumulates state as you scan left to right; each character is pushed and popped at most once → O(n).

**Monotonic stack**: also one pass. Each element is pushed once and popped at most once → O(n) total, even though there's a `while` loop inside the `for` loop. The amortized cost per element is O(1).

Multi-pass is rarely needed. One exception: if you need both "next greater to the left" and "next greater to the right" for each element, you can do two separate passes (left-to-right and right-to-left), each O(n).

## 6. Index and Pointer Management

- **Stack stores indices, not values** (for monotonic stack): storing indices lets you compute distances (`i - stack[-1]`) and look up values (`arr[stack[-1]]`)
- **Sentinel values**: appending a `0` at the end of a histogram array ensures all remaining stack entries get flushed in the final pass
- **Stack top access**: always check `if stack` before accessing `stack[-1]` to avoid IndexError on empty stack
- **Popping vs peeking**: `stack[-1]` peeks without removing; `stack.pop()` removes and returns — use peek when you need to check before deciding whether to pop

## 7. Complexity Patterns

| Variant | Time | Space |
|---|---|---|
| Regular stack (matching) | O(n) | O(n) worst case (all opens) |
| Regular stack (char processing) | O(n) | O(n) |
| Monotonic stack (next greater/smaller) | O(n) amortized | O(n) |
| Histogram largest rectangle | O(n) | O(n) |

The O(n) time for monotonic stack is amortized: each element is pushed once and popped once, so the total work across all iterations of the inner `while` loop is O(n).

## 8. Common Pitfalls

- **Forgetting to check empty stack before popping**: always guard with `if stack` or `if stack and condition`
- **Storing values instead of indices in monotonic stack**: you often need the index to compute distances or spans — store `i`, look up `arr[i]`
- **Wrong comparison direction**: decreasing stack → pop when `arr[i] > arr[stack[-1]]` (next greater); increasing stack → pop when `arr[i] < arr[stack[-1]]` (next smaller) — mixing these up gives wrong results
- **Not flushing the stack after the loop**: for histogram and similar problems, elements remaining in the stack after the main loop still need to be processed
- **Regular vs monotonic confusion**: if you're matching pairs or undoing operations, use a regular stack; if you're finding nearest greater/smaller, use monotonic — they look similar but serve different purposes
- **Returning stack contents vs derived result**: for "next greater element", the result array is built during pops, not by reading the final stack state
