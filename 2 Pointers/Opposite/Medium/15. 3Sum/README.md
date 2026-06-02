# 15. 3Sum

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/3sum/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Sort + fix one element + opposite-direction two pointers on the remaining subarray, with index checks to skip duplicates in-place.

## 2. How to Recognize the Pattern

- **Find all unique triplets that sum to zero**: This can be reduced to the 2Sum problem on a sorted array by fixing one element and using a two-pointer scan for the other two.
- **No duplicate triplets**: Sorting the input allows us to skip duplicate adjacent values for the fixed element and the two pointer positions, avoiding duplicate triplet entries.
- **Brute force complexity is too high**: $O(N^3)$ is too slow. Sorting enables a two-pointer scan that reduces the time complexity to $O(N^2)$.

## 3. Why This Algorithm Fits

- **$O(N^2)$ time**: Sorting takes $O(N \log N)$ time. Fixing the first element and executing an inner two-pointer scan takes $O(N)$ per iteration, resulting in $O(N^2)$ total time.
- **$O(1)$ space**: Runs entirely in-place (excluding space used by the sorting algorithm and the output list), avoiding the overhead of hash sets or lookup tables.
- **Ordered search**: In a sorted array, we can safely advance `left` if the sum is too small or retreat `right` if it is too large.

## 4. How It Works

Sort `nums` first. Loop through `nums` using index `i` as the fixed element:
1. If `i > 0` and `nums[i] == nums[i-1]`, skip the iteration to avoid duplicate triplets starting with the same value.
2. Initialize `left = i + 1` and `right = len(nums) - 1`.
3. While `left < right`:
   - Compute `summation = nums[i] + nums[left] + nums[right]`.
   - If `summation < 0`, increment `left`.
   - If `summation > 0`, decrement `right`.
   - If `summation == 0`, record the triplet. Increment `left`, decrement `right`, and run inner loops to skip duplicate values for both `left` and `right`.

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort array
        nums.sort()

        # Find triplets
        triplets = []
        nums_len = len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left = i+1
            right = nums_len - 1

            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                if summation < 0:
                    left +=1
                elif summation > 0:
                    right -= 1
                else:
                    triples = [nums[i], nums[left], nums[right]]
                    triplets.append(triples)
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
        return triplets
```

### Dry Run Table
Input: `nums = [-4, -1, -1, 0, 1, 2]` (sorted)

| i | nums[i] | left | right | summation | Action | triplets |
|---|---|---|---|---|---|---|
| 0 | -4 | 1 | 5 | -4 + -1 + 2 = -3 | $<0 \to$ `left = 2` | `[]` |
| 0 | -4 | 2 | 5 | -4 + -1 + 2 = -3 | $<0 \to$ `left = 3` | `[]` |
| 0 | -4 | 3 | 5 | -4 + 0 + 2 = -2 | $<0 \to$ `left = 4` | `[]` |
| 0 | -4 | 4 | 5 | -4 + 1 + 2 = -1 | $<0 \to$ `left = 5` | `[]` |
| 0 | -4 | 5 | 5 | — | `left >= right` $\to$ next `i` | `[]` |
| 1 | -1 | 2 | 5 | -1 + -1 + 2 = 0 | Match $\to$ add, update pointers | `[[-1, -1, 2]]` |
| 1 | -1 | 3 | 4 | -1 + 0 + 1 = 0 | Match $\to$ add, update pointers | `[[-1, -1, 2], [-1, 0, 1]]` |
| 1 | -1 | 4 | 3 | — | `left >= right` $\to$ next `i` | `[[-1, -1, 2], [-1, 0, 1]]` |
| 2 | -1 | — | — | — | `nums[2] == nums[1]` $\to$ skip | `[[-1, -1, 2], [-1, 0, 1]]` |

Result: `[[-1, -1, 2], [-1, 0, 1]]`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N^2)$ where $N$ is the number of elements in `nums`. Sorting takes $O(N \log N)$ time. The outer loop runs $N$ times, and the inner two-pointer traversal takes $O(N)$ time per iteration, yielding $O(N^2)$ total time.
- **Space Complexity**: $O(1)$ auxiliary space if we exclude the space allocated for the output array and sorting recursion stack.
