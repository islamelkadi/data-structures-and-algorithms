## 1. Algorithm Used

Reverse iteration with carry propagation — add 1 from the least significant digit and carry forward only when a digit overflows from 9 to 0.

## 2. How to Recognize the Pattern

- "Increment a number represented as a digit array" → simulate addition with carry → iterate from the back.
- The only special case is a chain of 9s — every 9 becomes 0 and the carry propagates left.
- If carry survives past index 0, the number was all 9s → prepend a 1.

## 3. Why This Algorithm Fits

- O(n) time — single right-to-left pass, early exit on the first non-9 digit.
- O(1) space — modified in-place; the `insert(0, 1)` case is O(n) but only happens once and only for all-9 inputs.
- No integer conversion needed — operating directly on the digit array avoids overflow issues with large inputs.

## 4. How It Works

Walk from the last digit backward. If the current digit is less than 9, increment it and stop — no carry needed. If it is 9, set it to 0 and continue (carry propagates). After the loop, if `carry` is still True every digit was 9 and is now 0, so prepend a 1.

```python
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

Input: `digits = [1, 2, 9]`

| i | digits[i] | < 9? | action | digits | carry |
|---|-----------|------|--------|--------|-------|
| 2 | 9 | no | set 0, carry=True | [1,2,0] | True |
| 1 | 2 | yes | +1, carry=False, break | [1,3,0] | False |
| result | | | | [1,3,0] | |

Input: `digits = [9, 9, 9]`

| i | digits[i] | < 9? | action | digits | carry |
|---|-----------|------|--------|--------|-------|
| 2 | 9 | no | set 0, carry=True | [9,9,0] | True |
| 1 | 9 | no | set 0, carry=True | [9,0,0] | True |
| 0 | 9 | no | set 0, carry=True | [0,0,0] | True |
| post | — | — | insert 1 at front | [1,0,0,0] | |

## 5. Time & Space Complexity

Time: O(n) — at most one full pass through the digits.

Space: O(1) extra — in-place modification; the all-9s case allocates one new element.
