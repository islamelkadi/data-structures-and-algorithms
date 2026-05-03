# 344. Reverse String

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/reverse-string/

## 1. Algorithm Used

Opposite-direction two pointers: swap characters from both ends moving inward until the pointers meet.

## 2. How to Recognize the Pattern

- "Reverse in-place" → swap from both ends → opposite-direction two pointers.
- Input is a character array and must be modified in-place → no new string allocation.
- Symmetric operation (first ↔ last, second ↔ second-to-last) → left/right pointers converging toward the middle.

## 3. Why This Algorithm Fits

- O(n) time — each element is touched exactly once (n/2 swaps).
- O(1) space — swaps are done in-place with a single temporary variable.
- The problem is purely symmetric, so converging pointers are the natural fit.

## 4. How It Works

Place `left_index` at 0 and `right_index` at the last position. Swap the characters at both pointers, then advance `left_index` forward and retreat `right_index` backward. Repeat until the pointers cross. At that point every character has been swapped with its mirror.

```python
left_index = 0
right_index = len(s) - 1
while left_index < right_index:
    s[left_index], s[right_index] = s[right_index], s[left_index]
    left_index += 1
    right_index -= 1
```

The loop runs exactly `len(s) // 2` times — the middle element (if any) never needs to move.
