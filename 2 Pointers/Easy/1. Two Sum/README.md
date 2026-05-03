## 1. Algorithm Used

Single-pass Hash Map lookup.

## 2. How to Recognize the Pattern

- "Find two numbers that sum to a target" → pair matching → hash map.
- Needs indices, not values → hash map naturally stores value → index.
- Brute force is O(n²), but the pair relationship is simple arithmetic (target - num), so a hash map drops it to O(n).

## 3. Why This Algorithm Fits

- O(n) time, O(n) space — one pass, one lookup per element.
- Sorting would lose original indices. Hash map avoids that.
- Exactly one solution guaranteed, so returning on first match is safe.

## 4. How It Works

For each number, compute the complement (`target - num`). If the complement is already in the map, return both indices. Otherwise, store the current number and index, and move on.

```python
hashmap = {}
for i, num in enumerate(nums):
    component = target - num
    if component in hashmap:
        return [hashmap[component], i]
    hashmap[num] = i
```

By the time you reach the second number of the pair, the first is already stored. You only ever look back.