# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Read/Write two pointers (fast & slow).

## 2. How to Recognize the Pattern

- **Remove duplicates in-place**: Modifying the array in-place with a strict space constraint points to the read/write two pointers design.
- **Sorted array**: Since duplicates are always adjacent, comparing `nums[slow]` with `nums[fast]` is sufficient to detect duplicate values.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Requires a single pass through the array.
- **$O(1)$ space**: Runs entirely in-place, using only two index variables.
- Sorted input guarantees that we only ever write each unique element once, without needing a hash set.

## 4. How It Works

`slow` is the write pointer, which tracks the boundary of the deduplicated prefix. `fast` is the read pointer scanning each element of the array.
1. When `nums[fast]` is different from `nums[slow]`, we have encountered a new unique value.
2. Increment `slow` by 1 and write the value `nums[fast]` to `nums[slow]`.
3. The count of unique elements is `slow + 1`.

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
```

### Dry Run Table
Input: `nums = [1, 1, 2, 3, 3]`

| fast | nums[fast] | slow | nums[slow] | action | array state |
|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | same $\to$ skip | `[1, 1, 2, 3, 3]` |
| 1 | 1 | 0 | 1 | same $\to$ skip | `[1, 1, 2, 3, 3]` |
| 2 | 2 | 0 | 1 | diff $\to$ `slow = 1`, write 2 | `[1, 2, 2, 3, 3]` |
| 3 | 3 | 1 | 2 | diff $\to$ `slow = 2`, write 3 | `[1, 2, 3, 3, 3]` |
| 4 | 3 | 2 | 3 | same $\to$ skip | `[1, 2, 3, 3, 3]` |

Result: `3` (First 3 elements: `[1, 2, 3]`)

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. We perform a single traversal of the input array.
- **Space Complexity**: $O(1)$ auxiliary space as we modify the array in-place.
