# 150. Evaluate Reverse Polish Notation

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Stack-based expression evaluation.

## 2. How to Recognize the Pattern

- **Evaluate Reverse Polish Notation**: Postfix notation is evaluated using a stack.
- **Operator follows operands**: In postfix, operands come first, operator comes after. We push operands onto a stack, pop the top two when we encounter an operator, evaluate the sub-expression, and push the result back.
- **Consuming and producing**: Same push-back-onto-stack pattern seen in decode string and asteroid collision.

## 3. Why This Algorithm Fits

- RPN is designed to be evaluated with a stack — no parentheses or operator precedence rules are needed.
- Each operator consumes exactly two operands from the top of the stack and produces one result.
- Order of evaluation matters for `-` and `/`: the first popped element is the right operand (`a`), and the second popped element is the left operand (`b`). That is why we evaluate `b - a` and `b / a`, not `a - b` or `a / b`.

## 4. How It Works

Walk through `tokens`. If a token is a number, push it onto the stack. If a token is an operator, pop two values, apply the operation, and push the result back. The final remaining value on the stack is the answer.

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
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
                # Note: do not do b // a because this will always
                # round down to the lowest nearest negative. If you
                # have positive numbers then no problem, but if you
                # have negatives and did -7 / -2 you will end up with
                # -4 instead of -3
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return stack.pop()
```

Note on `+` and `*`: Since addition and multiplication are commutative, order does not matter, so `stack.pop() + stack.pop()` and `stack.pop() * stack.pop()` are safe to write directly.

Note on `/`: `int(float(b) / a)` truncates toward zero in Python. Using `b // a` would floor-divide toward negative infinity, which yields incorrect results for negative numbers (e.g., `-7 // 2 = -4` instead of `-3`).

### Dry Run Table
Input: `tokens = ["2", "1", "+", "3", "*"]`

| token | action | stack |
|---|---|---|
| "2" | push 2 | `[2]` |
| "1" | push 1 | `[2, 1]` |
| "+" | pop 1, pop 2, push 3 | `[3]` |
| "3" | push 3 | `[3, 3]` |
| "*" | pop 3, pop 3, push 9 | `[9]` |
| result | pop | `[]` (Return `9`) |

Result: `9`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of tokens. We process each token once, and stack pushes/pops run in $O(1)$ time.
- **Space Complexity**: $O(N)$ auxiliary space for the stack, which holds at most $N/2$ operands in the worst case (e.g. all numbers at the beginning).
