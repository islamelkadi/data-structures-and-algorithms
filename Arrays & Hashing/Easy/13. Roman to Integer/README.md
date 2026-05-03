# 13. Roman to Integer
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/roman-to-integer/

## 1. Algorithm Used

Hash map lookup with a subtraction rule — subtract when a smaller value precedes a larger one.

## 2. How to Recognize the Pattern

- "convert Roman numeral string to integer" → map each symbol to its value → handle subtractive pairs.
- The subtractive rule (IV=4, IX=9, etc.) is the only special case; all others are additive.

## 3. Why This Algorithm Fits

- O(n) time — single left-to-right pass through the string.
- O(1) space — the value map has a fixed 7 entries.
- Comparing each character to the next handles all subtractive cases uniformly.

## 4. How It Works

Map each Roman symbol to its integer value. Iterate left to right: if the current symbol's value is less than the next symbol's value, subtract it; otherwise add it.

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and val[s[i]] < val[s[i+1]]:
                result -= val[s[i]]
            else:
                result += val[s[i]]
        return result
```

The subtractive cases (IV, IX, XL, XC, CD, CM) are all handled by the single condition `val[s[i]] < val[s[i+1]]` — no need to enumerate them explicitly.
