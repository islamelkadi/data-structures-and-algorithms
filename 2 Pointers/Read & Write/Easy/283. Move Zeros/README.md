# 283. Move Zeroes

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/move-zeroes/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Same-direction two pointers (`left` and `right`) with explicit case-based state branching.

## 2. How to Recognize the Pattern

- **In-place partition**: Reordering elements in-place based on a condition (zero vs non-zero) suggests two pointers moving in the same direction.
- **Maintain order of elements**: The non-zero elements must keep their relative order. Scanning from left to right and swapping elements preserves order.
- **Constant space restriction**: No auxiliary array is allowed, necessitating in-place swaps.

## 3. Why This Algorithm Fits

- The algorithm uses two pointers: `left` tracks the next target position (often zero) and `right` scans ahead.
- Iterating with case-based transitions guarantees that every element is processed in $O(1)$ comparisons per step, leading to $O(N)$ overall time.
- In-place swaps avoid allocating new array space.

## 4. How It Works

We initialize `left = 0` and `right = 1`. We iterate while `right < len(nums)`:
1. **Case 1**: `nums[left] == 0` and `nums[right] != 0` $\to$ Swap elements, increment both `left` and `right` (we've successfully moved a non-zero element left).
2. **Case 2**: `nums[left] != 0` and `nums[right] == 0` $\to$ Increment both `left` and `right` (no swap needed, current position is already non-zero).
3. **Case 3**: `nums[left] != 0` and `nums[right] != 0` $\to$ Increment both `left` and `right`.
4. **Case 4**: `nums[left] == 0` and `nums[right] == 0` $\to$ Increment `right` only (we need to scan further ahead to find a non-zero element to swap with the zero at `left`).

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while right <= len(nums) - 1: # Needed to move the very last index of the array
            # Check if left index == 0 and right index != 0
                # Switch
                # increment both left and right
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right += 1

            # Check if left index != 0 and right index == 0:
                # No switch
                # increment both left and right
            elif nums[left] != 0 and nums[right] == 0:
                left +=1
                right += 1

            # Check if left index != 0 and right index != 0:
                # No switch
                # increment both left and right
            elif nums[left] != 0 and nums[right] != 0:
                left +=1
                right += 1

            # Check if left index == 0 and right index == 0:
                # No switch
                # increment right
            else:
                right += 1
```

### Dry Run Table
Input: `nums = [0, 1, 0, 3, 12]`

| left | right | nums[left] | nums[right] | Case / Action | Array State |
|------|-------|------------|-------------|---------------|-------------|
| 0    | 1     | 0          | 1           | `nums[left] == 0` & `nums[right] != 0` $\to$ Swap, `left++`, `right++` | `[1, 0, 0, 3, 12]` |
| 1    | 2     | 0          | 0           | `nums[left] == 0` & `nums[right] == 0` $\to$ `right++` | `[1, 0, 0, 3, 12]` |
| 1    | 3     | 0          | 3           | `nums[left] == 0` & `nums[right] != 0` $\to$ Swap, `left++`, `right++` | `[1, 3, 0, 0, 12]` |
| 2    | 4     | 0          | 12          | `nums[left] == 0` & `nums[right] != 0` $\to$ Swap, `left++`, `right++` | `[1, 3, 12, 0, 0]` |
| 3    | 5     | —          | —           | `right > 4` $\to$ Terminate | `[1, 3, 12, 0, 0]` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. We scan through the array with the `right` pointer exactly once.
- **Space Complexity**: $O(1)$ auxiliary space since we perform all swaps in-place.
