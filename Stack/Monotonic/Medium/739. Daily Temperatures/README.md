## 1. Algorithm Used

Monotonic decreasing stack.

## 2. How to Recognize the Pattern

- "How many days until a warmer temperature?" → for each element, find the next greater element → monotonic stack.
- Anytime you need "next greater/smaller element" for every item in an array, think monotonic stack.
- Brute force is O(n²) — for each day, scan forward. The stack processes each element at most twice (push + pop), giving O(n).

## 3. Why This Algorithm Fits

- The stack maintains a decreasing sequence of temperatures. When a warmer day arrives, it resolves all cooler days waiting on the stack.
- Each day is pushed once and popped once — no redundant comparisons.
- Days that never find a warmer temperature stay on the stack and keep their default value of 0.

## 4. How It Works

Walk through temperatures. For each day, while the stack's top is cooler than today, pop it — today is the answer for that popped day. Record the distance (`i - index`). Then push today onto the stack.

```python
temperature_tracker = [0] * len(temperatures)
stack = []
for i in range(len(temperatures)):
    while stack and stack[-1][0] < temperatures[i]:
        _, index = stack.pop()
        temperature_tracker[index] = i - index
    stack.append((temperatures[i], i))
return temperature_tracker
```

Example with `[73, 74, 75, 71, 69, 72, 76, 73]`:
- Push 73(0)
- 74 > 73 → pop, tracker[0] = 1. Push 74(1)
- 75 > 74 → pop, tracker[1] = 1. Push 75(2)
- 71 < 75 → push 71(3)
- 69 < 71 → push 69(4)
- 72 > 69 → pop, tracker[4] = 1. 72 > 71 → pop, tracker[3] = 2. Push 72(5)
- 76 > 72 → pop, tracker[5] = 1. 76 > 75 → pop, tracker[2] = 4. Push 76(6)
- 73 < 76 → push 73(7)
- Result: `[1, 1, 4, 2, 1, 1, 0, 0]`

## 5. Time & Space Complexity

Time: O(n) — each element is pushed and popped at most once. The while loop across all iterations does at most n pops total.

Space: O(n) — the stack holds at most n elements (if temperatures are strictly decreasing), plus the output array.
