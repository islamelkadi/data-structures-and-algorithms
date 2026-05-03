## 1. Algorithm Used

Monotonic stack with time-to-target calculation.

## 2. How to Recognize the Pattern

- "How many groups arrive together?" → cars that catch up merge into fleets → monotonic stack.
- Sorting by position (closest to target first) lets you process cars in the order they'd encounter each other.
- A slower car (higher arrival time) blocks faster cars behind it → only push when a car is slower than the fleet ahead.

## 3. Why This Algorithm Fits

- After sorting by position descending, each car only needs to compare against the fleet directly ahead (top of stack).
- If a car arrives faster (less or equal time) than the fleet ahead, it merges — don't push.
- If it's slower (more time), it forms a new fleet — push it.
- The stack ends up holding one entry per fleet.

## 4. How It Works

Pair positions with speeds, sort by position descending (closest to target first). For each car, calculate time to reach target. If it's slower than the fleet ahead (top of stack), it's a new fleet — push. Otherwise it merges — skip.

```python
zipped_positions_speed = [(x1, x2) for x1, x2 in zip(position, speed)]
zipped_positions_speed.sort(reverse=True)

stack = []
for car in zipped_positions_speed:
    current_time = (target - car[0]) / float(car[-1])
    if not stack or current_time > stack[-1]:
        stack.append(current_time)
return len(stack)
```

Example with `target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]`:
```
Sorted by position desc: [(10,2), (8,4), (5,1), (3,3), (0,1)]

(10,2): time = 1.0  → stack empty, push. Stack = [1.0]
(8,4):  time = 1.0  → 1.0 > 1.0? No → merges. Stack = [1.0]
(5,1):  time = 7.0  → 7.0 > 1.0? Yes → new fleet. Stack = [1.0, 7.0]
(3,3):  time = 3.0  → 3.0 > 7.0? No → merges. Stack = [1.0, 7.0]
(0,1):  time = 12.0 → 12.0 > 7.0? Yes → new fleet. Stack = [1.0, 7.0, 12.0]

Result: 3 fleets
```

Python 2 gotcha: `/ float(car[-1])` ensures float division. Without it, `4 / 3 = 1` in Python 2 instead of `1.333`.

## 5. Time & Space Complexity

Time: O(n log n) — sorting dominates. The stack loop is O(n) since each car is visited once with no popping.

Space: O(n) — for the zipped list and the stack.
