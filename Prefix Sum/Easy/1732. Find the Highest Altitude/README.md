## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Prefix sum of a gain array with running maximum tracking.

## 2. How to Recognize the Pattern

- "Altitude changes" or "net gain" array → reconstruct absolute values via prefix sum.
- "Find the highest point" → track the running maximum as you accumulate.
- Starting altitude is 0 and not given explicitly → initialize both `curr` and `max_alt` to 0.

## 3. Why This Algorithm Fits

- O(n) time — single pass through the gain array.
- O(1) space — only two variables needed: current altitude and maximum seen.
- The gain array is a difference array; prefix-summing it reconstructs the original altitude sequence.

## 4. How It Works

Start at altitude 0. For each gain value, add it to the current altitude and update the maximum if the new altitude is higher. The answer is the maximum altitude seen, including the starting altitude of 0 (which handles the case where all gains are negative).

```python
max_alt = curr = 0
for g in gain:
    curr += g
    max_alt = max(max_alt, curr)
return max_alt
```

Initializing `max_alt` to 0 correctly accounts for the starting point — if every gain is negative, the highest altitude is the starting altitude of 0.

Input: `gain = [-5, 1, 5, 0, -7]`

| i | gain[i] | curr | max_alt |
|---|---------|------|---------|
| init | — | 0 | 0 |
| 0 | -5 | -5 | 0 |
| 1 | 1 | -4 | 0 |
| 2 | 5 | 1 | 1 |
| 3 | 0 | 1 | 1 |
| 4 | -7 | -6 | 1 |
| result | | | 1 |
