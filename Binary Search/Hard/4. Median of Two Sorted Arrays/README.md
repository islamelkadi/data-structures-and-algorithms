# 4. Median of Two Sorted Arrays

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Merging and sorting two sorted arrays followed by element selection.

## 2. How to Recognize the Pattern

- **Find the median of two sorted arrays**: Indicates combining arrays and identifying the middle element (or average of two middle elements).
- While an $O(\log(M+N))$ partitioning binary search algorithm exists, merging and sorting the combined lists offers a highly readable, straightforward approach.

## 3. Why This Algorithm Fits

- Extremely simple and readable compared to partitioning binary search.
- Handles all edge cases (empty lists, negative values, duplicates) natively through python's `sorted()` implementation.

## 4. How It Works

1. Combine the two sorted arrays `nums1` and `nums2` and sort the result to form `nums3`.
2. Check the parity of the length of `nums3`:
   - If the length is even, find the two middle elements, take their average, and return it.
   - If the length is odd, return the middle element.

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+nums2)
        
        if len(nums3)%2==0:
            return float((nums3[len(nums3)//2-1] + nums3[len(nums3)//2])/2)
        else:
            return float(nums3[len(nums3)//2])
```

### Dry Run Table
Input: `nums1 = [1, 3]`, `nums2 = [2]`

- Combined list: `nums1 + nums2 = [1, 3, 2]`
- Sorted list `nums3 = [1, 2, 3]`
- `len(nums3) = 3` (odd)

| Array `nums3` | Length | Middle Index (`len // 2`) | Element at Index |
|---|---|---|---|
| `[1, 2, 3]` | 3 | 1 | `nums3[1] = 2` |

Result: `2.0`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O((M + N) \log(M + N))$ where $M$ and $N$ are the sizes of `nums1` and `nums2` respectively. Sorting the combined list of size $M+N$ dominates the time complexity.
- **Space Complexity**: $O(M + N)$ auxiliary space to allocate and store the combined array `nums3`.
