# 88. Merge Sorted Array

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/merge-sorted-array/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Three-pointer merge from the back (single loop).

## 2. How to Recognize the Pattern

- **Merge two sorted arrays in-place**: This is similar to the merge step in merge sort.
- **Pre-allocated space at tail**: `nums1` has extra space at the end, suggesting we should fill from the back to avoid overwriting unprocessed elements.
- **Avoid element shifting**: Merging from the front would require shifting elements on every insert — $O(N^2)$ time. Back to front avoids that overhead.

## 3. Why This Algorithm Fits

- The empty slots at the end of `nums1` give us a safe place to write.
- By placing the largest elements first, the write position is always in the "empty" zone or already processed.
- **Single loop**: The `nums1_ptr >= 0` guard handles `nums1` exhaustion inline — when `nums1` runs out, the `else` block keeps copying from `nums2` until it's done.
- Truly in-place, requiring no extra array.

## 4. How It Works

Three pointers starting at the back. Compare elements from both arrays, place the larger one at the combined pointer. The `nums1_ptr >= 0` guard ensures you don't access `nums1` out of bounds — when `nums1` is exhausted, the `else` takes over and copies remaining `nums2` elements. Loop ends when `nums2` is fully placed. `nums1` leftovers are already in position.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_ptr = m - 1
        nums2_ptr = n - 1
        nums1_nums2_combined_ptr = m + n - 1

        while nums2_ptr >= 0:
            if nums1_ptr >= 0 and nums1[nums1_ptr] > nums2[nums2_ptr]:
                nums1[nums1_nums2_combined_ptr] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[nums1_nums2_combined_ptr] = nums2[nums2_ptr]
                nums2_ptr -= 1
            nums1_nums2_combined_ptr -= 1
```

Example with `nums1 = [1, 2, 3, 0, 0, 0]`, $m=3$, `nums2 = [2, 5, 6]`, $n=3$:
```
Start: nums1_ptr=2, nums2_ptr=2, nums1_nums2_combined_ptr=5

nums1[2]=3 vs nums2[2]=6 → else: place 6. nums1=[1,2,3,_,_,6]. nums2_ptr=1
nums1[2]=3 vs nums2[1]=5 → else: place 5. nums1=[1,2,3,_,5,6]. nums2_ptr=0
nums1[2]=3 vs nums2[0]=2 → if: place 3.   nums1=[1,2,3,3,5,6]. nums1_ptr=1
nums1[1]=2 vs nums2[0]=2 → else: place 2. nums1=[1,2,2,3,5,6]. nums2_ptr=-1

nums2_ptr < 0 → loop ends. Result: [1,2,2,3,5,6]
```

Why only loop while `nums2_ptr >= 0`? If `nums2` is done, `nums1`'s remaining elements are already sorted and in place — nothing to move. If `nums1` runs out first, the `else` branch keeps firing and copies the rest of `nums2`.

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(M + N)$ where $M$ and $N$ are the sizes of `nums1` and `nums2`. Each element is placed exactly once.
- **Space Complexity**: $O(1)$ auxiliary space as we only use three pointer variables.
