# 1. Two Sum

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/two-sum/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Single-pass Hash Map lookup.

## 2. How to Recognize the Pattern

- **"Find two numbers that sum to a target"**: Pair matching problem where we need to find a relationship between two elements.
- **Indices needed**: Since the output requires indices rather than values, storing the value-to-index mapping in a hash map is a natural fit.
- **Unsorted input**: Sorting would lose the original indices, so a hash map is preferred to find the complement in $O(1)$ time while preserving order.

## 3. Why This Algorithm Fits

- **$O(N)$ Time**: Drops the time complexity from the brute-force $O(N^2)$ to $O(N)$ by doing single-pass lookups.
- **$O(N)$ Space**: The hash map stores the elements and their corresponding indices as we iterate.
- **One-Pass**: We look back at previously stored elements for a match, ensuring we find the solution in a single scan.

## 4. How It Works

For each number `num` at index `i`, we compute its complement: `complement = target - num`. 
- If the `complement` exists in the hash map, we have found the matching pair. We immediately return the index of the complement and the current index `i`.
- Otherwise, we store the current number in the hash map with its index: `hashmap[num] = i`.

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
```

### Dry Run Table
Input: `nums = [2, 7, 11, 15]`, `target = 9`

| i | num | complement | hashmap | action |
|---|-----|------------|---------|--------|
| 0 | 2 | 7 | `{}` | `7` not in map $\to$ store `{2: 0}` |
| 1 | 7 | 2 | `{2: 0}` | `2` in map $\to$ return `[0, 1]` |

Result: `[0, 1]`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. We traverse the list containing $N$ elements exactly once. Each lookup in the hash map takes $O(1)$ time.
- **Space Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. In the worst case, we might store up to $N - 1$ elements in the hash map before finding a match.
