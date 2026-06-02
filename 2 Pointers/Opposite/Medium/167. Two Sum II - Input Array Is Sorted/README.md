# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Opposite-direction two pointers on a sorted array: converge based on whether the current sum is below or above the target.

## 2. How to Recognize the Pattern

- **Sorted array search**: "Find two numbers in a sorted array that sum to target" suggests using two pointers at both ends of the array.
- **Monotonic relationship**: Since the array is sorted, incrementing the left pointer increases the sum, and decrementing the right pointer decreases the sum.
- **1-indexed result**: The output expects 1-based indexing instead of the standard 0-based array index.

## 3. Why This Algorithm Fits

- The pointers move inward without backtracking, ensuring a single linear scan of $O(N)$ time.
- No hash map or other data structures are needed, achieving $O(1)$ auxiliary space.

## 4. How It Works

1. Initialize `left = 0` and `right = len(numbers) - 1`.
2. While `left < right`:
   - Calculate `summation = numbers[left] + numbers[right]`.
   - If `summation < target`, increment `left` to increase the sum.
   - If `summation > target`, decrement `right` to decrease the sum.
   - If `summation == target`, return `[left + 1, right + 1]`.

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            summation = numbers[left] + numbers[right]
            if summation < target:
                left += 1
            elif summation > target:
                right -= 1
            else:
                return [left + 1, right + 1]
```

### Dry Run Table
Input: `numbers = [2, 7, 11, 15]`, `target = 9`

| left | right | numbers[left] | numbers[right] | sum | action |
|------|-------|---------------|----------------|-----|--------|
| 0    | 3     | 2             | 15             | 17  | $> 9 \to$ `right--` |
| 0    | 2     | 2             | 11             | 13  | $> 9 \to$ `right--` |
| 0    | 1     | 2             | 7              | 9   | $== 9 \to$ Return `[1, 2]` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `numbers`. Each pointer moves at most $N$ times.
- **Space Complexity**: $O(1)$ auxiliary space as we only use two integer indices.
