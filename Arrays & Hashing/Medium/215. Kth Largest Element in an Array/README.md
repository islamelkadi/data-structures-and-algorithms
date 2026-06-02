# 215. Kth Largest Element in an Array

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Max-Heap (Priority Queue) using negated values to simulate a max-heap with Python's default min-heap `heapq`.

## 2. How to Recognize the Pattern

- **K-th largest/smallest element**: Finding the $k$-th extreme value in an unsorted collection suggests using a heap or the QuickSelect algorithm.
- **Dynamic extraction**: Building a heap of size $N$ allows us to extract the maximum elements one by one. By extracting $k - 1$ times, the next root of the heap will be the $k$-th largest element.

## 3. Why This Algorithm Fits

- Python's `heapq` is a min-heap. We can negate all values in the input array to transform it into a max-heap representation.
- Heapifying the array takes $O(N)$ time.
- Popping $k-1$ times from the heap takes $O(k \log N)$ time, which is highly efficient if $k$ is small.
- *Note*: If $k \approx N$, this approach degrades to $O(N \log N)$ time complexity, which is equivalent to full sorting.

## 4. How It Works

1. Negate all numbers in the input: `nums = [-n for n in nums]`.
2. Convert the list into a min-heap: `heapq.heapify(nums)` ($O(N)$ time).
3. Pop the root element $k - 1$ times: `heapq.heappop(nums)`. The heap self-corrects after each pop to maintain its structure.
4. The root element at index 0 of the heap is now the $k$-th largest element in negated form. Return `-nums[0]`.

```python
import heapq
import math

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Since largest is required, converting list to negative
        nums = [-n for n in nums]
        heapq.heapify(nums)

        # Note in previous submissions you were trying to find the
        # index of the target node using the formula for 0-indexed
        # array -> left: 2N + 1 | right: 2N + 2
        # Heaps are not sorted in the sense of traditional sorted
        # arrays, so you cannot rely on that mechanism. Instead,
        # when you pop an element, the heap will recorrect itself
        # to maintain the proper heap tree structure. So in theory,
        # if you pop k - 1 times (because you still want to arrive
        # at that Kth element, so make sure to not pop that out) you
        # will theoritically have the kth's largest element as the
        # root of the tree

        # NOTE: I hate to break it to you, but this is at worst case
        # O(nlog(n)). In other words, there is not difference between
        # 1) heapifying this
        # and
        # 2) doing a nums.sorted(reverse=True) and then picking nums[k]
        for _ in range(k - 1):
            heapq.heappop(nums)
        
        return -nums[0]
```

### Dry Run Example
Input: `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`
1. Negated list: `[-3, -2, -1, -5, -6, -4]`
2. Heapified list: `[-6, -5, -4, -2, -1, -3]` (root is `-6`)
3. Extracting $k-1 = 1$ time:

| Step | Heap State (Min-Heap representation) | Pop Value | New Heap Root | Details |
|---|---|---|---|---|
| 1 | `[-6, -5, -4, -2, -1, -3]` | `-6` | `-5` | Root `-6` popped; heap reheapifies. |

4. Return `-nums[0]` = `-(-5)` = `5`.

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N + k \log N)$ where $N$ is the number of elements in `nums`. Building the heap takes $O(N)$ time, and each of the $k - 1$ pop operations takes $O(\log N)$ time.
- **Space Complexity**: $O(N)$ space to store the negated elements in-place.
