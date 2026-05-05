# 26. Remove Duplicates from Sorted Array
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## 1. Algorithm Used

Read/Write two pointers (fast & slow).

## 2. How to Recognize the Pattern

- "Remove duplicates in-place" + sorted array → read/write pointers.
- The array is sorted, so duplicates are always adjacent — no need for a hash set.
- O(1) space constraint rules out building a new array; in-place modification with a write pointer is the right move.

## 3. Why This Algorithm Fits

- O(n) time — single pass through the array.
- O(1) space — no extra data structures, just two index variables.
- Sorted input guarantees that comparing `nums[slow]` to `nums[fast]` is enough to detect a new unique value.

## 4. How It Works

`slow` is the write pointer — it marks the boundary of the deduplicated prefix. `fast` scans every element. When `fast` finds a value different from `nums[slow]`, a new unique element has been found: advance `slow` and overwrite `nums[slow]` with it.

```python
slow = 0
for fast in range(len(nums)):
    if nums[slow] != nums[fast]:
        slow += 1
        nums[slow] = nums[fast]
return slow + 1
```

At the end, `slow` is the index of the last unique element, so the count of unique elements is `slow + 1`. The elements beyond that index don't matter.

Input: `nums = [1, 1, 2, 3, 3]`

| fast | nums[fast] | slow | nums[slow] | action | array |
|------|------------|------|------------|--------|-------|
| 0 | 1 | 0 | 1 | same → skip | [1,1,2,3,3] |
| 1 | 1 | 0 | 1 | same → skip | [1,1,2,3,3] |
| 2 | 2 | 0 | 1 | diff → slow=1, write 2 | [1,2,2,3,3] |
| 3 | 3 | 1 | 2 | diff → slow=2, write 3 | [1,2,3,3,3] |
| 4 | 3 | 2 | 3 | same → skip | [1,2,3,3,3] |
| result | | 2 | | return slow+1=3 | |
