# 13. Roman to Integer

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/roman-to-integer/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Hash map lookup with running sum subtraction — subtract double the previous value when a smaller symbol precedes a larger one.

## 2. How to Recognize the Pattern

- **Convert Roman numeral string to integer**: Map symbols (`I`, `V`, `X`, `L`, `C`, `D`, `M`) to values.
- **Subtractive pairs**: The subtractive rule (e.g., `IV = 4`, `IX = 9`) occurs when a smaller Roman numeral is placed before a larger one. 

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Requires a single left-to-right pass through the string.
- **$O(1)$ space**: The Roman numeral symbol mapping has a fixed size of 7 elements.
- The running sum subtraction logic (`summation -= previous * 2`) allows us to process the string from left to right without looking ahead, keeping the logic clean and fast.

## 4. How It Works

Map each Roman numeral character to its integer value.
Traverse the string from left to right:
1. If the current symbol's value is greater than the `previous` symbol's value:
   - We must undo the previous addition and perform the subtraction. We do this in one step by subtracting `previous * 2` from the running `summation`.
2. Add the current symbol's value to `summation`.
3. Set `previous = current_val`.

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_symbol_reference = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Approach 1 - stack
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        # stack = []
        # for char_ in s:
        #     if stack and roman_symbol_reference[char_] > stack[-1]:
        #         stack.append(roman_symbol_reference[char_] - stack.pop())
        #     else:
        #         stack.append(roman_symbol_reference[char_])
        # return sum(stack)

        # Time Complexity: O(N)
        # Space Complexity: O(1)
        previous = summation = 0
        for char_ in s:
            if roman_symbol_reference[char_] > previous:
                # Logic here is to FIRST undo the addition of previous integer
                # Then add the difference between the current integer and the one before it

                # Instead of doing summation -= previous then roman[char_] - previous
                # you can do - (previous * 2) since you are subtracting previous twice
                summation -= previous * 2
            summation += roman_symbol_reference[char_]
            previous = roman_symbol_reference[char_]
        return summation
```

### Dry Run Table
Input: `s = "MCMXCIV"` ($1994$)

| char\_ | value | previous | value > previous? | adjustment (`summation -= previous * 2`) | summation |
|---|---|---|---|---|---|
| *init* | — | 0 | — | — | 0 |
| `"M"` | 1000 | 0 | yes | `summation -= 0` | 1000 |
| `"C"` | 100 | 1000 | no | *None* | 1100 |
| `"M"` | 1000 | 100 | yes | `summation -= 200` | 1900 |
| `"X"` | 10 | 1000 | no | *None* | 1910 |
| `"C"` | 100 | 10 | yes | `summation -= 20` | 1990 |
| `"I"` | 1 | 100 | no | *None* | 1991 |
| `"V"` | 5 | 1 | yes | `summation -= 2` | 1994 |

Result: `1994`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of `s`. We traverse the string once, and lookup and math operations run in $O(1)$ time.
- **Space Complexity**: $O(1)$ auxiliary space as we only use a few helper variables, and the mapping reference size is fixed.
