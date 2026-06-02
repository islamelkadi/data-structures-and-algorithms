# 219. Contains Duplicate II

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/contains-duplicate-ii/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Fixed-size sliding window of size $k$ backed by a hash set to detect duplicate elements within the window in $O(1)$ lookup time.

## 2. How to Recognize the Pattern

- **Distance constraint on duplicates**: "Two indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`" indicates duplicate detection within a sliding window of max size $k$.
- **Window eviction**: We maintain a set representing the current active window. If the size of the set exceeds $k$, we remove the oldest element (`nums[i - k]`) to slide the window.

## 3. Why This Algorithm Fits

- Using a hash set gives $O(1)$ membership checks (`if nums[i] in window`).
- Because we only keep up to $k$ elements in the set, the memory usage is bounded by $O(k)$ rather than storing the index of every element in the array ($O(N)$ space).

## 4. How It Works

1. Initialize a hash set `window` to track elements in the current window.
2. Iterate through `nums` using index `i`:
   - If `nums[i]` is already in `window`, return `True` (a duplicate exists within distance $k$).
   - Add `nums[i]` to `window`.
   - If the size of `window` exceeds `k`, remove `nums[i - k]` (the element that is no longer in range).
3. If the loop completes without finding a duplicate, return `False`.

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k]) # left index = i - k
        return False
```

### Dry Run Table
Input: `nums = [1, 2, 3, 1]`, `k = 3`

| i | nums[i] | In window? | Action | Window State |
|---|---------|------------|--------|--------------|
| 0 | 1       | no         | Add    | `{1}` |
| 1 | 2       | no         | Add    | `{1, 2}` |
| 2 | 3       | no         | Add    | `{1, 2, 3}` |
| 3 | 1       | yes        | Duplicate found $\to$ return `True` | — |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. We perform a single pass over the array and do $O(1)$ set lookups, insertions, and deletions.
- **Space Complexity**: $O(\min(N, K))$ auxiliary space as the `window` set stores at most $K$ elements at any given time.
