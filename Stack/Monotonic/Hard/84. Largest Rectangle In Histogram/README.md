## 1. Algorithm Used

Monotonic increasing stack (no padding variant).

## 2. How to Recognize the Pattern

- "Largest rectangle in histogram" → for each bar, find how far it can extend left and right → next smaller element on both sides → monotonic stack.
- Same "next greater/smaller" pattern as daily temperatures, but applied to area calculation.
- When you see "maximize a rectangle under constraints" in a 1D array, think monotonic stack.

## 3. Why This Algorithm Fits

- The stack maintains bars in increasing height order. When a shorter bar arrives, all taller bars on the stack have found their right boundary — pop and compute area.
- Left boundary is the bar remaining on top of the stack after popping (the nearest shorter bar to the left).
- The flush loop handles bars that never found a shorter bar to their right — their right boundary is the end of the array.
- Empty stack after a pop means the popped bar was the shortest so far — it extends all the way to index 0, so `width = i` (or `len(heights)` during flush).

## 4. How It Works

Push bars in increasing order. When a shorter bar arrives, pop taller bars and compute their area using:
- Right boundary: current index `i`
- Left boundary: `stack[-1]` index (nearest shorter bar to the left), or index 0 if stack is empty
- Width: `right - left - 1`, or just `i` if no left boundary

After the main loop, flush remaining bars using `len(heights)` as the right boundary.

```python
stack = []
max_area = 0
for i, current_height in enumerate(heights):
    while stack and stack[-1][0] > current_height:
        popped_height, index = stack.pop()
        width = i if not stack else i - stack[-1][-1] - 1
        max_area = max(max_area, popped_height * width)
    stack.append((current_height, i))

while stack:
    popped_height, index = stack.pop()
    width = len(heights) if not stack else len(heights) - stack[-1][-1] - 1
    max_area = max(max_area, popped_height * width)

return max_area
```

Example with `heights = [2, 1, 5, 6, 2, 3]`:
```
i=0: push (2,0). Stack = [(2,0)]
i=1: 1 < 2 → pop (2,0). Stack empty → width = 1. Area = 2. Push (1,1). Stack = [(1,1)]
i=2: push (5,2). Stack = [(1,1),(5,2)]
i=3: push (6,3). Stack = [(1,1),(5,2),(6,3)]
i=4: 2 < 6 → pop (6,3). width = 4-2-1 = 1. Area = 6.
     2 < 5 → pop (5,2). width = 4-1-1 = 2. Area = 10.
     Push (2,4). Stack = [(1,1),(2,4)]
i=5: push (3,5). Stack = [(1,1),(2,4),(3,5)]

Flush:
  pop (3,5). width = 6-4-1 = 1. Area = 3.
  pop (2,4). width = 6-1-1 = 4. Area = 8.
  pop (1,1). Stack empty → width = 6. Area = 6.

Max area = 10
```

## 5. Time & Space Complexity

Time: O(n) — each bar is pushed once and popped once across both loops.

Space: O(n) — stack holds at most n bars (if heights are strictly increasing).
