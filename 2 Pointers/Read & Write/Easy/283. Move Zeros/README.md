# 283. Move Zeroes

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/move-zeroes/

## 1. Algorithm Used

Same-direction two pointers: slow pointer tracks the next write position, fast pointer scans for non-zero elements.

## 2. How to Recognize the Pattern

- "Move all zeroes to the end" → partition in-place → slow/fast pointer where slow marks the write head.
- In-place rearrangement with no extra array → two pointers in the same direction.
- Order of non-zero elements must be preserved → scan left to right, write left to right.

## 3. Why This Algorithm Fits

- O(n) time — single pass through the array.
- O(1) space — swaps done in-place, no auxiliary storage.
- Swapping (rather than shifting) avoids the O(n²) cost of repeatedly shifting elements left.

## 4. How It Works

`slow_pointer` starts at 0 and marks where the next non-zero value should land. The fast pointer `i` iterates through every element. Whenever `nums[i]` is non-zero, it swaps with `nums[slow_pointer]` and advances `slow_pointer`. This pushes non-zeros to the front in their original order while zeroes naturally accumulate at the back.

```python
slow_pointer = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[slow_pointer] = nums[slow_pointer], nums[i]
        slow_pointer += 1
```

After the loop, all elements before `slow_pointer` are non-zero (in original order) and everything from `slow_pointer` onward is zero.

Input: `nums = [0, 1, 0, 3, 12]`

| i | nums[i] | slow_pointer | action | array |
|---|---------|--------------|--------|-------|
| 0 | 0 | 0 | zero → skip | [0,1,0,3,12] |
| 1 | 1 | 0 | non-zero → swap [0]↔[1], slow=1 | [1,0,0,3,12] |
| 2 | 0 | 1 | zero → skip | [1,0,0,3,12] |
| 3 | 3 | 1 | non-zero → swap [1]↔[3], slow=2 | [1,3,0,0,12] |
| 4 | 12 | 2 | non-zero → swap [2]↔[4], slow=3 | [1,3,12,0,0] |
