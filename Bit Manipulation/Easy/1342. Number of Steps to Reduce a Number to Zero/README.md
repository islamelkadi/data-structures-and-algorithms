# 1342. Number of Steps to Reduce a Number to Zero

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)
5. [Bitwise Perspective](#5-bitwise-perspective)

## 1. Algorithm Used

The algorithm simulates the step-by-step reduction of a number to zero. At each step, if the number is even, it divides it by 2; if the number is odd, it subtracts 1.

## 2. How to Recognize the Pattern

- **Repeated Division / Reduction**: The problem defines a deterministic sequence of operations to apply to a number until it hits zero. This is a direct simulation pattern.
- **Logarithmic Reduction**: Halving a number on even values means the number of digits/bits decreases quickly. The operations are bounded by the binary size of the input.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(\log N)$ where $N$ is the value of `num`. Since we halve the number at least every two steps, the number of steps is proportional to the number of bits in `num` ($\approx \log_2 N$).
- **Space Complexity**: $O(1)$ auxiliary space.

## 4. How It Works

1. Initialize `operations = 0`.
2. While `num` is not 0:
   - If `num` is even, divide it by 2 (using integer division `num // 2`).
   - If `num` is odd, subtract 1.
   - Increment `operations` by 1.
3. Return `operations`.

```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        def process_number(n: int) -> int:
            return n // 2 if n % 2 == 0 else n - 1
    
        operations = 0
        while num != 0:
            num = process_number(num)
            operations += 1
        return operations
```

### Dry Run Table
Input: `num = 14`

| Step | Current `num` | Condition (`num % 2 == 0`) | Next `num` | `operations` | Action Taken |
|------|---------------|----------------------------|------------|--------------|--------------|
| *init*| 14           | —                          | 14         | 0            | Start loop |
| 1    | 14            | Even (True)                | 7          | 1            | Divide by 2 |
| 2    | 7             | Even (False)               | 6          | 2            | Subtract 1 |
| 3    | 6             | Even (True)                | 3          | 3            | Divide by 2 |
| 4    | 3             | Even (False)               | 2          | 4            | Subtract 1 |
| 5    | 2             | Even (True)                | 1          | 5            | Divide by 2 |
| 6    | 1             | Even (False)               | 0          | 6            | Subtract 1 |

---

## 5. Bitwise Perspective

In binary terms, the operations correspond to:
- **Even (ends in `0`)**: Dividing by 2 is a right shift (`num >> 1`), which removes the trailing `0`. This takes **1 step**.
- **Odd (ends in `1`)**: Subtracting 1 changes the trailing `1` to `0`. This takes **1 step**. (The next step will then be a division/right shift to remove that `0`).

Hence, the total number of operations is:
$$\text{Total Steps} = (\text{Total Bits in Binary} - 1) + (\text{Number of Set 1 Bits})$$
For example, $14$ in binary is `1110` (4 bits, three `1`s):
$$\text{Total Steps} = (4 - 1) + 3 = 6 \text{ steps}$$
This enables an alternative $O(1)$ time bitwise count solution:
```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        binary_str = bin(num)[2:]
        return len(binary_str) - 1 + binary_str.count('1')
```
