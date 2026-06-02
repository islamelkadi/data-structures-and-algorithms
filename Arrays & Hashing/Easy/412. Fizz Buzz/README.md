# 412. Fizz Buzz

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/fizz-buzz/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Linear iteration with modulo checks — check divisibility by 15 first, then 5, then 3, to avoid double-counting.

## 2. How to Recognize the Pattern

- "Replace multiples of 3 and 5 with labels" → modulo arithmetic → iterate and check each number.
- Divisibility by both 3 and 5 must produce "FizzBuzz" → check `% 15` before the individual checks, or the combined case gets shadowed.
- Output is a list of strings in order → single pass, append to result.

## 3. Why This Algorithm Fits

- O(n) time — one pass through 1 to n.
- O(n) space — the output list holds n strings.
- Checking `% 15` first is the simplest way to handle the combined case without nested conditions or string concatenation.

## 4. How It Works

Iterate from 1 to n inclusive. For each number, test divisibility in order of specificity: `% 15` (both), then `% 5` (Buzz), then `% 3` (Fizz), then fall through to the number itself as a string. Append the result to the answer list.

```python
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 5 == 0:
                ans.append("Buzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            else:
                ans.append(str(i))
        return ans
```

The order of checks matters: if you test `% 3` or `% 5` first, multiples of 15 would match the wrong branch before reaching "FizzBuzz".

Input: `n = 5`

| i | i%15 | i%5 | i%3 | output |
|---|------|-----|-----|--------|
| 1 | 1 | 1 | 1 | "1" |
| 2 | 2 | 2 | 2 | "2" |
| 3 | 3 | 3 | 0 | "Fizz" |
| 4 | 4 | 4 | 1 | "4" |
| 5 | 5 | 0 | 2 | "Buzz" |
