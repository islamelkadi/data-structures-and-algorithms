# 239. Sliding Window Maximum

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/sliding-window-maximum/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Max-Heap (Priority Queue) with lazy deletion and index-based boundary validation.

## 2. How to Recognize the Pattern

- **Dynamic maximum in a sliding window**: Finding the maximum value in every contiguous sliding window of size $k$ requires tracking the largest value while dropping elements that fall out of bounds.
- **Heap with lazy deletion**: Instead of $O(N)$ removal of arbitrary expired elements inside a queue, we use a heap and only pop elements from the top if they fall outside the current window bounds.

## 3. Why This Algorithm Fits

- Python's `heapq` is a min-heap by default. By storing values as `-nums[i]`, we simulate a max-heap.
- Tuples are compared lexicographically: by storing elements as `(-nums[i], -i)`, we resolve duplicates in favor of the larger index (since `-idx` is smaller for a larger index `idx`, making it smaller in the min-heap). This ensures the element that stays in the window longest has priority.

## 4. How It Works

1. Initialize a heap with the first $k$ elements as `(-nums[i], -i)`.
2. Append the current maximum value `-heap[0][0]` to `max_elements`.
3. Iterate `i` from $k$ to `len(nums) - 1`:
   - Push `(-nums[i], -i)` onto the heap.
   - Check the top of the heap. While the index of the top element `-heap[0][1]` is outside the current window (i.e. $\le i - k$), pop it.
   - Append `-heap[0][0]` to `max_elements`.
4. Return `max_elements`.

```python
import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # # First attempt
        # max_elements = []
        # nums = [-x for x in nums]
        # for i in range(0, len(nums) - k + 1):
        #     heap = nums[i : i + k]
        #     heapq.heapify(heap)
        #     max_elements.append(-heap[0])
        # return max_elements

        # Second attempt - more optimized
        # Step 1
        # Notice that we are using the heap
        # to store the element and its index
        # this is because heaps behave lexograpically
        # and you don't want to lose the duplicate entry
        # incase the list had a duplicate entry. The fact
        # that you need to find the max heap and that heaps
        # allow lexographic comparision is why we also made
        # the index negative so that if the first entry is
        # a duplicate, then you do a lexographic comparison
        # on the second entry and you choose the bigger one
        # accordingly to be the heap max. If the question
        # wanted min heap, then you won't need to do a negative
        # number nor a negative index, you would use it as is.
        # Python's heapq doesn't support max heap, hence the
        # negative addition
        if k == 1:
            return nums

        heap = []
        heapq.heapify(heap)
        for i in range(k):
            heapq.heappush(heap, (-nums[i], -i))

        # Add max element
        max_elements = [-heap[0][0]]

        # Step 2
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], -i))

            # This means that the left most boundary's index
            # is still greater than that of the current heap
            # max. This means the heap is no longer within
            # bounds
            while i - k >= -heap[0][1]:
                heapq.heappop(heap)

            max_elements.append(-heap[0][0])
        return max_elements
```

### Dry Run Table
Input: `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`

| i | nums[i] | Pushed | Heap Top `(val, idx)` | Valid? `idx > i - 3` | Action | Result List |
|---|---------|--------|-----------------------|----------------------|--------|-------------|
| *init* | — | — | `(-3, -1)` (value 3, index 1) | — | — | `[3]` |
| 3 | -3 | `(3, -3)` | `(-3, -1)` (value 3, index 1) | $1 > 0$ (Yes) | No pop | `[3, 3]` |
| 4 | 5 | `(-5, -4)` | `(-5, -4)` (value 5, index 4) | $4 > 1$ (Yes) | No pop | `[3, 3, 5]` |
| 5 | 3 | `(-3, -5)` | `(-5, -4)` (value 5, index 4) | $4 > 2$ (Yes) | No pop | `[3, 3, 5, 5]` |
| 6 | 6 | `(-6, -6)` | `(-6, -6)` (value 6, index 6) | $6 > 3$ (Yes) | No pop | `[3, 3, 5, 5, 6]` |
| 7 | 7 | `(-7, -7)` | `(-7, -7)` (value 7, index 7) | $7 > 4$ (Yes) | No pop | `[3, 3, 5, 5, 6, 7]` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N \log N)$ where $N$ is the number of elements in `nums`. In the worst case (ascending array), every element is pushed onto the heap, taking $O(\log N)$ time per push/pop.
- **Space Complexity**: $O(N)$ to store all elements and their indices in the heap.
