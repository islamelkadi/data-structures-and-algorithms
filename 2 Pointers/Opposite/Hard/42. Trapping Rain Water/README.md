# 42. Trapping Rain Water

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/trapping-rain-water/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Two-pointer converging search. We maintain left and right pointers moving inward, keeping track of the running maximum heights from both sides (`max_left` and `max_right`).

## 2. How to Recognize the Pattern

- **Calculating cumulative water capacity trapped between barriers**: The water trapped at any position `i` is determined by `min(max_left, max_right) - height[i]`.
- **Finding boundaries dynamically**: Instead of precomputing prefix and suffix max arrays, we can dynamically converge two pointers inward from the boundaries.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Single pass where the two pointers converge.
- **$O(1)$ space**: Only a few scalar variables for tracking indices and max heights, avoiding the $O(N)$ auxiliary prefix/suffix arrays.
- **Bottleneck-driven updates**: Since we don't know during runtime what obstacles lie ahead, we bring the side with the smaller boundary inwards. The larger boundary on the opposite side ensures that any water trapped is only constrained by the smaller side's running maximum.

## 4. How It Works

Initialize `left = 0`, `right = len(height) - 1`, and running boundaries `max_left = max_right = trapped = 0`. At each step:
1. Update `max_left` with `height[left]` and `max_right` with `height[right]`.
2. If `max_left < max_right`, the left boundary is the bottleneck. The water trapped at `left` is `max_left - height[left]`. Add this to the total, then increment `left`.
3. Otherwise, the right boundary is the bottleneck. The water trapped at `right` is `max_right - height[right]`. Add this to the total, then decrement `right`.

```python
# TWO_POINTERS

# NOTE: YOU NEED TO KEEP IN MIND YOU DO NOT KNOW `DURING RUNTIME` IF THERE ARE
# OBSTACLES. HENCE, YOU NEED TO BRING THE LEFT INWARDS IF THE RIGHT IS BIGGER
# THAN IT SO YOU CAN EXPLORE POTENTIALLY STORING MORE WATER. AND THE SAME APPLIES
# TO THE RIGHT SIDE.

# THE ONLY WAY YOU CAN KNOW UP FRONT WHAT YOUR OBSTACLES ARE IS IF YOU USE A 
# PREFIX SUM APPROACH TO TRACK OBSTACLES FROM THE LEFT, AND SUFFIX SUM APPROACH
# TO TRACK OBSTACLES FROM THE RIGHT.

class Solution:
    def trap(self, height: List[int]) -> int:

        # SLIDING_WINDOW APPROACH
        right = len(height) - 1
        left = max_left = max_right = trapped = 0

        while left < right:
            current_left = height[left]
            current_right = height[right]

            max_left = max(max_left, current_left)
            max_right = max(max_right, current_right)

            if max_left < max_right:
                trapped += max_left - current_left
                left += 1
            else:
                trapped += max_right - current_right
                right -= 1

        return trapped
```

### Dry Run Table
Input: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`

| Step | left | right | max_left | max_right | Check (max_left < max_right) | trapped increment | trapped |
|---|---|---|---|---|---|---|---|
| init | 0 | 11 | 0 | 0 | — | — | 0 |
| 1 | 0 | 11 | 0 | 1 | 0 < 1 (True) | 0 - 0 = 0 | 0 |
| 2 | 1 | 11 | 1 | 1 | 1 < 1 (False) | 1 - 1 = 0 | 0 |
| 3 | 1 | 10 | 1 | 2 | 1 < 2 (True) | 1 - 1 = 0 | 0 |
| 4 | 2 | 10 | 1 | 2 | 1 < 2 (True) | 1 - 0 = 1 | 1 |
| 5 | 3 | 10 | 2 | 2 | 2 < 2 (False) | 2 - 2 = 0 | 1 |
| 6 | 3 | 9 | 2 | 2 | 2 < 2 (False) | 2 - 1 = 1 | 2 |
| 7 | 3 | 8 | 2 | 2 | 2 < 2 (False) | 2 - 2 = 0 | 2 |
| 8 | 3 | 7 | 2 | 3 | 2 < 3 (True) | 2 - 2 = 0 | 2 |
| 9 | 4 | 7 | 2 | 3 | 2 < 3 (True) | 2 - 1 = 1 | 3 |
| 10 | 5 | 7 | 2 | 3 | 2 < 3 (True) | 2 - 0 = 2 | 5 |
| 11 | 6 | 7 | 2 | 3 | 2 < 3 (True) | 2 - 1 = 1 | 6 |
| 12 | 7 | 7 | Loop terminates (`left == right`) | | | | 6 |

Result: `6`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `height`. Pointers `left` and `right` converge in a single pass.
- **Space Complexity**: $O(1)$ auxiliary space as we only store a few boundary and accumulator variables.
