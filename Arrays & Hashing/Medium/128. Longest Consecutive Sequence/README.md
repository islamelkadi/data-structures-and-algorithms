# 128. Longest Consecutive Sequence

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/longest-consecutive-sequence/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Hash Set with sequence-start detection — only begin counting a run from `num` when `num - 1` is absent from the set, ensuring each sequence is counted exactly once.

## 2. How to Recognize the Pattern

- **Find the longest consecutive sequence**: Need to identify connected runs of numbers.
- **O(n) time requirement**: Sorting is too slow ($O(N \log N)$), which points to using a hash set for $O(1)$ membership checks.
- **Identify sequence starts**: To avoid redundant counting, we only begin tracking a sequence if its predecessor (`num - 1`) is not present in the set.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Each number is visited at most twice (once in the main loop, and at most once in the inner `while` loop across all sequence traversals).
- **$O(N)$ space**: For the hash set.
- Iterating over the set instead of the original array avoids processing duplicates.
- `subarr_len` is initialized inside the `if` block, resetting correctly for each new sequence.

## 4. How It Works

Put all numbers in a set. For each number, check if it's the start of a sequence (`num - 1` not in set). If it is, walk forward with `num + 1` counting consecutive elements. Track the longest run found.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Logic:
        # Create a hashset of all the items in the list
        # Iterate through each entry in the hashset, and find
        # out which ones do not have an n-1 in the hashset.
        # Those will be your starting points, and you can enforce
        # the starting point check via an if condition to continue
        # into the logic if that particular number does not have a
        # n-1.

        # Once you've passed the check, from there:
            # 1. Initialize a counter of len 1
            # 2. Check if n+1 exists in hashset
            # 3. If yes increment the subarr_len
            # 4. Increment num
            # 5. Iterate to the next num
        nums_hashset = set(nums)
        ans = 0
        for num in nums_hashset:
            if num - 1 not in nums_hashset:
                subarr_len = 1
                while num + 1 in nums_hashset:
                    subarr_len += 1
                    num += 1
                ans = max(ans, subarr_len)
        return ans
```

### Dry Run Table
Input: `nums = [100, 4, 200, 1, 3, 2]` $\to$ set: `{1, 2, 3, 4, 100, 200}`

| num | num-1 in set? | sequence walk | length | ans |
|---|---|---|---|---|
| 100 | 99? no $\to$ start | 101? no | 1 | 1 |
| 4 | 3? yes $\to$ skip | — | — | 1 |
| 200 | 199? no $\to$ start | 201? no | 1 | 1 |
| 1 | 0? no $\to$ start | 2✓ $\to$ 3✓ $\to$ 4✓ $\to$ 5? no | 4 | 4 |
| 3 | 2? yes $\to$ skip | — | — | 4 |
| 2 | 1? yes $\to$ skip | — | — | 4 |

Result: `4`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. Building the hash set takes $O(N)$ time. Since we only start a sequence walk when `num - 1` is not in the set, each element in the set is visited at most twice. Thus, the overall time complexity is linear.
- **Space Complexity**: $O(N)$ auxiliary space to store the unique elements of `nums` in the hash set.
