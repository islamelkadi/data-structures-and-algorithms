# 11. Container With Most Water

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/container-with-most-water/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Two-pointer greedy shrink from both ends.

## 2. How to Recognize the Pattern

- **Maximize area between two lines**: The area depends on two variables: width (distance between indices) and height (the shorter of the two boundary lines).
- **Inward scanning**: Starting at the maximum possible width (the extreme ends of the array) and shrinking inward allows us to systematically evaluate promising pairs.
- **Greedy pointer movement**: An $O(N^2)$ brute force can be optimized to $O(N)$ by moving only the pointer pointing to the shorter line.

## 3. Why This Algorithm Fits

- The shorter line is the bottleneck limiting the area. Moving the pointer at the shorter line is the only action that could find a taller partner and increase the area.
- Moving the pointer at the taller side would only decrease the width without any possibility of increasing the constraining height.
- This greedy elimination guarantees we never bypass the maximum possible area.

## 4. How It Works

Start with `left = 0` and `right = len(height) - 1` (maximum width). Compute the area as `min(height[left], height[right]) * (right - left)`.
1. Update `maximum_area` if the `current_area` is larger.
2. Move the pointer pointing to the shorter line inward.
3. Repeat until `left` and `right` meet.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = current_area = maximum_area = 0
        right = len(height) - 1

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maximum_area = max(maximum_area, current_area)
        return maximum_area
```

### Dry Run Table
Input: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

| left | right | height[left] | height[right] | current_area | maximum_area | Action |
|---|---|---|---|---|---|---|
| 0 | 8 | 1 | 7 | $1 \times 8 = 8$ | 8 | `height[left] < height[right]` $\to$ `left += 1` |
| 1 | 8 | 8 | 7 | $7 \times 7 = 49$ | 49 | `height[left] >= height[right]` $\to$ `right -= 1` |
| 1 | 7 | 8 | 3 | $3 \times 6 = 18$ | 49 | `height[left] >= height[right]` $\to$ `right -= 1` |
| 1 | 6 | 8 | 8 | $8 \times 5 = 40$ | 49 | `height[left] >= height[right]` $\to$ `right -= 1` |
| 1 | 5 | 8 | 4 | $4 \times 4 = 16$ | 49 | `height[left] >= height[right]` $\to$ `right -= 1` |
| 1 | 4 | 8 | 5 | $5 \times 3 = 15$ | 49 | `height[left] >= height[right]` $\to$ `right -= 1` |
| 1 | 3 | 8 | 2 | $2 \times 2 = 4$ | 49 | `height[left] >= height[right]` $\to$ `right -= 1` |
| 1 | 2 | 8 | 6 | $6 \times 1 = 6$ | 49 | `height[left] >= height[right]` $\to$ `right -= 1` |
| 1 | 1 | — | — | — | 49 | `left >= right` $\to$ stop |

Result: `49`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of lines. Each step moves one pointer inward, resulting in at most $N - 1$ steps.
- **Space Complexity**: $O(1)$ auxiliary space as we only store scalar variables.
