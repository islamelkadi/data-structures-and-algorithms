## 1. Algorithm Used

Read & write two pointers with a duplicate count tracker.

## 2. How to Recognize the Pattern

- "Remove in-place, allow at most k duplicates" → read & write pointers.
- Sorted array means duplicates are always adjacent → a simple counter suffices.
- `left` is the write pointer, `i` (right) is the read pointer.

## 3. Why This Algorithm Fits

- Single pass, O(n) time and O(1) space.
- The count resets on every new value, so it naturally enforces the "at most 2" rule.

## 4. How It Works

`left` starts at 1 (first position is always valid). `count` tracks consecutive duplicates of the current value. For each element `i`, if it equals the previous element increment `count`, otherwise reset to 1. If `count <= 2`, write `nums[i]` to `nums[left]` and advance `left`.

```python
left = 1
count = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        count += 1
    else:
        count = 1
    if count <= 2:
        nums[left] = nums[i]
        left += 1
return left
```

Example with `nums = [1,1,1,2,2,3]`:
- i=1: 1==1, count=2, <=2 → write, left=2
- i=2: 1==1, count=3, >2 → skip
- i=3: 2!=1, count=1, <=2 → write, left=3
- i=4: 2==2, count=2, <=2 → write, left=4
- i=5: 3!=2, count=1, <=2 → write, left=5
- Result: `[1,1,2,2,3]`, return 5

Input: `nums = [1,1,1,2,2,3]`

| i | nums[i] | nums[i-1] | count | count<=2? | left | nums (write head) |
|---|---------|-----------|-------|-----------|------|-------------------|
| 1 | 1 | 1 | 2 | yes | 2 | [1,1,1,2,2,3] |
| 2 | 1 | 1 | 3 | no | 2 | skip |
| 3 | 2 | 1 | 1 | yes | 3 | [1,1,2,2,2,3] |
| 4 | 2 | 2 | 2 | yes | 4 | [1,1,2,2,2,3] |
| 5 | 3 | 2 | 1 | yes | 5 | [1,1,2,2,3,3] |
| result | | | | | 5 | [1,1,2,2,3,...] |

## 5. Time & Space Complexity

Time: O(n) — single pass.

Space: O(1) — in-place, no extra data structures.
