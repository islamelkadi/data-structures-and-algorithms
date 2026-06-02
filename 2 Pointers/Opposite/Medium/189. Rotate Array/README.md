# 189. Rotate Array

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/rotate-array/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Three-reverse technique with modulo optimization: rotate the entire array, then reverse two distinct subarrays in-place.

## 2. How to Recognize the Pattern

- **Cyclic rotation in-place**: "Rotate the array to the right by $k$ steps in-place" suggests utilizing symmetry operations (like reversals) instead of shifting elements one-by-one.
- **Unbounded step counts**: The rotation steps $k$ can exceed the array size, necessitating modulo normalization: `k = k % len(nums)`.

## 3. Why This Algorithm Fits

- Rotating elements individually or using inserts (`nums.insert(0, nums.pop())`) takes $O(N \times K)$ time, causing Time Limit Exceeded for large inputs.
- The three-reverse approach reverses sections of the array in-place, achieving $O(N)$ time complexity and $O(1)$ auxiliary space.

## 4. How It Works

1. **Normalize $k$**: `k = k % len(nums)` to remove redundant full rotations.
2. **Reverse entire array**: Reverses the whole list so that the elements that should be at the front are now at the front (but in reverse order), and the elements that should be at the back are at the back (also in reverse order).
3. **Reverse first $k$ elements**: Re-reverses the first $k$ elements to restore their original relative order.
4. **Reverse remaining elements**: Re-reverses the remaining $n - k$ elements to restore their original relative order.

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Solution 1 - time exceeded
        # while k != 0:
        #     nums.insert(0, nums.pop())
        #     k -= 1
        # 
 
        # # Solution 2 - 2 pointers
        # nums.reverse()
        # k = k % len(nums)
        # left, right_1_ptr = 0, k - 1
        # k_ptr, right_2_ptr = k, len(nums) - 1

        # while left < right_1_ptr:
        #     nums[left], nums[right_1_ptr] = nums[right_1_ptr], nums[left]
        #     left += 1
        #     right_1_ptr -= 1
        
        # while k_ptr < right_2_ptr:
        #     nums[k_ptr], nums[right_2_ptr] = nums[right_2_ptr], nums[k_ptr]
        #     k_ptr += 1
        #     right_2_ptr -= 1

        # Solution 3 - 2 pointers abstracted
        nums.reverse()

        # Get pivot index
        k = k % len(nums)
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
```

### Understanding `k`: Step Count vs. Index
`k` represents a **count of rotation steps**, not an array index. While indices reference specific positions within the array (0-based), `k` quantifies how many times the entire array should be rotated to the right. For example, with `nums = [1,2,3,4,5]` and `k = 2`, we perform two complete rotation operations—not access the element at index 2. However, `k` indirectly determines index boundaries: after rotation, the last `k` elements (originally at indices `n-k` through `n-1`) move to the front, while the first `n-k` elements (indices `0` through `n-k-1`) shift to the back. In the three-reverse algorithm, we use `k` to split the array into two sections for reversal, but `k` itself remains a step counter—not an index value.

### Dry Run Table
Input: `nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`

| Step | Action | Slice/Range | Array State | Details |
|---|---|---|---|---|
| *init* | — | — | `[1, 2, 3, 4, 5, 6, 7]` | — |
| 1 | Reverse entire array | `0` to `n - 1` | `[7, 6, 5, 4, 3, 2, 1]` | `nums.reverse()` |
| 2 | Reverse first `k` elements | `0` to `k - 1` (0 to 2) | `[5, 6, 7, 4, 3, 2, 1]` | `nums[:3]` reversed |
| 3 | Reverse remaining elements | `k` to `n - 1` (3 to 6) | `[5, 6, 7, 1, 2, 3, 4]` | `nums[3:]` reversed |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. Reversing the array sections in-place visits each element a constant number of times.
- **Space Complexity**: $O(1)$ auxiliary space as the array is modified entirely in-place.
