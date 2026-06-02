# 66. Plus One

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/plus-one/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Reverse iteration with carry propagation — add 1 to the least significant digit and carry forward only when a digit overflows from 9 to 0.

## 2. How to Recognize the Pattern

- **Increment a number represented as a digit array**: Simulate addition with carry by iterating from the back of the array.
- **Carry propagation with 9s**: Any 9 becomes 0, and the carry propagates to the left.
- **Prepend carry**: If the carry survives past index 0, the number was composed entirely of 9s, so we must prepend a 1 to the array.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Single right-to-left pass, exiting early on the first non-9 digit.
- **$O(1)$ space**: Modified in-place; prepending 1 is $O(N)$ but only occurs once for all-9 inputs.
- **No integer overflow**: Operating directly on the digit array avoids overflow issues associated with large integer conversions.

## 4. How It Works

Walk from the last digit backward. If the current digit is less than 9, increment it and stop — no carry is needed. If the digit is 9, set it to 0 and continue to propagate the carry. After the loop, if the carry is still True (all digits were 9s and are now 0s), prepend a 1.

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                carry = False
                break
            digits[i] = 0
            carry = True
        if carry:
            digits.insert(0, 1)
        return digits
```

### Dry Run Table
Input: `digits = [1, 2, 9]`

| i | digits[i] | < 9? | action | digits state | carry |
|---|---|---|---|---|---|
| 2 | 9 | no | set 0, carry=True | `[1, 2, 0]` | True |
| 1 | 2 | yes | +1, carry=False, break | `[1, 3, 0]` | False |

Result: `[1, 3, 0]`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of `digits`. At most one full pass through the digit array is performed.
- **Space Complexity**: $O(1)$ auxiliary space as we modify the array in-place, except for allocating one new element when prepending the carry in the all-9s case.
