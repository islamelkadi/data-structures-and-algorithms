## 1. Algorithm Used

Stack-based expression evaluation.

## 2. How to Recognize the Pattern

- "Evaluate Reverse Polish Notation" → postfix expression → stack.
- In postfix, operands come first, operator comes after → push operands, pop two when you hit an operator, push the result back.
- Same push-back-onto-stack pattern as decode string and asteroid collision.

## 3. Why This Algorithm Fits

- RPN is designed to be evaluated with a stack — no parentheses, no precedence rules needed.
- Each operator consumes exactly two operands from the top of the stack and produces one result.
- Order matters for `-` and `/` — the first pop is the right operand, second pop is the left. That's why you do `b - a` and `b / a`, not `a - b`.

## 4. How It Works

Walk through tokens. If it's a number, push it. If it's an operator, pop two values, apply the operation, push the result back. The final value on the stack is the answer.

```python
stack = []
for token in tokens:
    if token == "+":
        stack.append(stack.pop() + stack.pop())
    elif token == "-":
        a, b = stack.pop(), stack.pop()
        stack.append(b - a)
    elif token == "*":
        stack.append(stack.pop() * stack.pop())
    elif token == "/":
        a, b = stack.pop(), stack.pop()
        stack.append(int(float(b) / a))
    else:
        stack.append(int(token))
return stack.pop()
```

Note on `+` and `*`: order doesn't matter (commutative), so `stack.pop() + stack.pop()` is fine without assigning to `a, b`.

Note on `/`: `int(float(b) / a)` truncates toward zero. `b // a` would round toward negative infinity, giving wrong results for negative numbers (e.g., `-7 // 2 = -4` instead of `-3`).

Example with `["2", "1", "+", "3", "*"]`:
- Push 2, 1
- `+`: pop 1, pop 2 → push 3
- Push 3
- `*`: pop 3, pop 3 → push 9
- Result: 9

## 5. Time & Space Complexity

Time: O(n) — single pass through tokens, each push/pop is O(1).

Space: O(n) — stack holds at most n/2 operands (in the worst case, all numbers come first).
