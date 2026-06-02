# 344. Reverse String

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/reverse-string/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Opposite-direction two pointers: swap characters from both ends moving inward until the pointers meet.

## 2. How to Recognize the Pattern

- **Reverse in-place**: Swap elements from both ends toward the middle using opposite-direction two pointers.
- **In-place array modification**: The input is a character array that must be modified without allocating extra space for another array.
- **Symmetric convergence**: Swapping index $i$ with index $n - 1 - i$ implies converging pointers `left` and `right`.

## 3. Why This Algorithm Fits

- The algorithm converges toward the middle, checking and swapping symmetric elements in $O(N)$ total time.
- By swapping in-place using a temporary variable, it avoids allocating extra memory, satisfying the $O(1)$ space constraint.

## 4. How It Works

1. Initialize `left_index` to 0 and `right_index` to `len(s) - 1`.
2. While `left_index < right_index`:
   - Store `s[left_index]` in a temporary variable `tmp`.
   - Assign `s[right_index]` to `s[left_index]`.
   - Assign `tmp` to `s[right_index]`.
   - Increment `left_index` and decrement `right_index`.

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_index = 0
        right_index = len(s) - 1
        
        while left_index < right_index:
            tmp = s[left_index]
            s[left_index] = s[right_index]
            s[right_index] = tmp
            left_index +=1
            right_index -= 1
```

### Dry Run Table
Input: `s = ["h","e","l","l","o"]`

| step | left | right | swap | array |
|------|------|-------|------|-------|
| 1    | 0    | 4     | h ↔ o | `["o","e","l","l","h"]` |
| 2    | 1    | 3     | e ↔ l | `["o","l","l","e","h"]` |
| 3    | 2    | 2     | `left >= right` → stop | `["o","l","l","e","h"]` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in array `s`. We make exactly $N / 2$ swaps.
- **Space Complexity**: $O(1)$ auxiliary space as we only use a single temporary variable `tmp` to swap elements in-place.
