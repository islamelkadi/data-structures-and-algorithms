# 88. Merge Sorted Array

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/merge-sorted-array/

## 1. Algorithm Used

Two pointers from the back, filling nums1 in reverse to avoid overwriting valid elements.

## 2. How to Recognize the Pattern

- "Merge in-place" + one array has extra space at the end → fill from the back → reverse two-pointer merge.

## 3. Why This Algorithm Fits

- O(m + n) time — each element is placed exactly once.
- O(1) space — merges directly into nums1's pre-allocated tail.

## 4. How It Works

Place one pointer at the last valid element of nums1 (index m-1), one at the last element of nums2 (index n-1), and a write pointer at the very end of nums1 (index m+n-1). At each step, write the larger of the two pointed-at values to the write position and advance that pointer backward. After the main loop, copy any remaining nums2 elements — remaining nums1 elements are already in place.

```python
p1, p2, p = m - 1, n - 1, m + n - 1
while p1 >= 0 and p2 >= 0:
    if nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]; p1 -= 1
    else:
        nums1[p] = nums2[p2]; p2 -= 1
    p -= 1
while p2 >= 0:
    nums1[p] = nums2[p2]; p2 -= 1; p -= 1
```

Filling from the back is the key insight — it guarantees you never overwrite an element in nums1 before it has been compared.
