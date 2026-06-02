# 27. Remove Element

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/remove-element/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Opposite-direction two pointers (swap-to-back partition).

## 2. How to Recognize the Pattern

- **Remove all occurrences of a value in-place**: Partition the array so that all non-target elements are shifted to the front.
- **Strict O(1) space constraint**: Swapping elements avoids allocating a new array.
- **Order does not need to be preserved**: This allows swapping target elements directly to the end of the array, which is faster and avoids shifting elements.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: The left and right pointers together traverse the array at most once.
- **$O(1)$ space**: Only two index variables are maintained.
- **Reduced writes**: Swapping instead of shifting avoids moving every subsequent element when the target value appears early.

## 4. How It Works

`right` starts at the end of the array and retreats past any trailing `val` elements. `left` scans forward from the beginning.
1. While `nums[right] == val`, decrement `right`.
2. If `left > right`, all elements have been processed, so we break.
3. If `nums[left] == val`, swap it with `nums[right]` (which is guaranteed to be a non-val element) and decrement `right`.
4. Otherwise, `left` advances.

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums) - 1
        for left in range(len(nums)):
            while nums[right] == val and right >= 0:
                right -= 1

            # Should be left > right instead of
            # left == right because you may have
            # have use cases where the list is even.
            # Therefore, you won't have a situation
            # where left == right when you right -= 1
            # and left += 1
            if left > right:
                break

            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        return right + 1
```

The break condition is `left > right` instead of `left == right` because in even-length arrays, the pointers can cross without ever being equal (when `right` decrements and `left` increments simultaneously).

### Dry Run Table
Input: `nums = [3, 2, 2, 3]`, `val = 3`

| step | left | right | nums[left] | nums[right] | action | list state |
|---|---|---|---|---|---|---|
| init | 0 | 3 | 3 | 3 | `right` retreats past trailing 3s | `[3, 2, 2, 3]` |
| 1 | 0 | 1 | 3 | 2 | `nums[left] == val` $\to$ swap $\to$ `right = 1` | `[2, 2, 3, 3]` |
| 2 | 1 | 1 | — | — | `left > right` $\to$ break | `[2, 2, 3, 3]` |

Result: `2` (First 2 elements: `[2, 2]`)

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. We traverse the array at most once.
- **Space Complexity**: $O(1)$ auxiliary space as we modify the array in-place.
