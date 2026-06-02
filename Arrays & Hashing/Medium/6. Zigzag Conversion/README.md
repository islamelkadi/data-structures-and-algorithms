# 6. Zigzag Conversion

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/zigzag-conversion/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Row simulation with a direction flag — distribute characters into row buckets by bouncing a row tracker up and down, then concatenate.

## 2. How to Recognize the Pattern

- **Rearrange characters in a zigzag pattern**: Simulates traversing a grid row-by-row. We can assign each character to its respective row bucket directly.
- **Oscillating row indices**: The row index moves from `0` to `numRows - 1` and then back to `0`, reversing direction whenever a boundary is hit.
- **Concat output rows**: Reading rows left-to-right means we can just concatenate the string contents of the row buckets at the end.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Single pass through the string `s`.
- **$O(N)$ space**: The row buckets collectively store all $N$ characters.
- Direct simulation is much cleaner and less error-prone than solving the arithmetic indices mathematically.

## 4. How It Works

We track the current row (`r_tracker`) and the direction flag (`is_down`). For each character in the string:
1. Append the character to `zig_zag[r_tracker]`.
2. Move `r_tracker` up or down based on `is_down`.
3. If `r_tracker` reaches `0` or `numRows - 1` (the boundaries), flip `is_down`.
4. A guard `numRows == 1` avoids infinite direction flipping at the only boundary.

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        r_tracker, is_down = 0, True
        zig_zag = ["" for _ in range(numRows)]
        for char_ in s:
            zig_zag[r_tracker] += char_
            r_tracker += 1 if is_down else -1

            # If you hit a boundary, then change direction
            if r_tracker in (0, numRows - 1):
                is_down = not is_down

        return "".join(zig_zag)
```

### Dry Run Table
Input: `s = "PAYPALISHIRING"`, `numRows = 3`

| char | r_tracker | is_down | zig_zag state |
|---|---|---|---|
| `"P"` | 0 | True (flip) | `["P", "", ""]` |
| `"A"` | 1 | True | `["P", "A", ""]` |
| `"Y"` | 2 | True (flip) | `["P", "A", "Y"]` |
| `"P"` | 1 | False | `["P", "AP", "Y"]` |
| `"A"` | 0 | False (flip) | `["PA", "AP", "Y"]` |
| `"L"` | 1 | True | `["PA", "APL", "Y"]` |
| `"I"` | 2 | True (flip) | `["PA", "APL", "YI"]` |
| `"S"` | 1 | False | `["PA", "APLS", "YI"]` |
| `"H"` | 0 | False (flip) | `["PAH", "APLS", "YI"]` |
| `"I"` | 1 | True | `["PAH", "APLSI", "YI"]` |
| `"R"` | 2 | True (flip) | `["PAH", "APLSI", "YIR"]` |
| `"I"` | 1 | False | `["PAH", "APLSII", "YIR"]` |
| `"N"` | 0 | False (flip) | `["PAHN", "APLSII", "YIR"]` |
| `"G"` | 1 | True | `["PAHN", "APLSIIG", "YIR"]` |

Result: `"PAHNAPLSIIGYIR"`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of string `s`. We traverse the string exactly once.
- **Space Complexity**: $O(N)$ auxiliary space as the row buckets store all $N$ characters of the string.
