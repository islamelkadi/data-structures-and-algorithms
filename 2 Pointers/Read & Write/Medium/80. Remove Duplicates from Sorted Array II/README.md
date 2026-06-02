# 80. Remove Duplicates from Sorted Array II

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Read & write two pointers with a duplicate count tracker.

## 2. How to Recognize the Pattern

- **Remove duplicates in-place, allowing at most k duplicates**: Enforces the read and write pointers design.
- **Sorted array**: Since duplicates are always adjacent, a simple running counter suffices to track frequency.
- `left` is the write pointer, and the loop index `i` is the read pointer.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Requires only a single pass through the array.
- **$O(1)$ space**: Runs entirely in-place.
- The duplicate count resets on every new value, so we naturally enforce the "at most 2 occurrences" rule.

## 4. How It Works

`left` starts at 1 (since the first element is always valid). `count` tracks consecutive duplicates of the current value. For each element starting from index 1:
1. If the current element equals the previous one, we increment `count`.
2. Otherwise, we reset `count` to 1.
3. If `count <= 2`, we write the current element to `nums[left]` and increment `left`.

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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

### Dry Run Table
Input: `nums = [1, 1, 1, 2, 2, 3]`

| i | nums[i] | nums[i-1] | count | count <= 2? | left | nums (current write state) |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | yes | 2 | `[1, 1, 1, 2, 2, 3]` |
| 2 | 1 | 1 | 3 | no | 2 | *skip* |
| 3 | 2 | 1 | 1 | yes | 3 | `[1, 1, 2, 2, 2, 3]` |
| 4 | 2 | 2 | 2 | yes | 4 | `[1, 1, 2, 2, 2, 3]` |
| 5 | 3 | 2 | 1 | yes | 5 | `[1, 1, 2, 2, 3, 3]` |

Result: `5` (First 5 elements: `[1, 1, 2, 2, 3]`)

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. We perform a single traversal of the input array.
- **Space Complexity**: $O(1)$ auxiliary space as we modify the array in-place.
