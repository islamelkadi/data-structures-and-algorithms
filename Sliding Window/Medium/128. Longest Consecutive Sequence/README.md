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

Hash set with sequence-start detection — only begin counting a run from `num` when `num - 1` is absent from the set, ensuring each sequence is counted exactly once.

## 2. How to Recognize the Pattern

- **longest consecutive sequence** with $O(N)$ time requirement $\to$ sorting is too slow ($O(N \log N)$) $\to$ hash set for $O(1)$ membership checks.
- **Avoid re-counting**: Only start scanning from the smallest element of each run (where `num - 1` is not in the set).
- **No index constraint**: No subarray/contiguous constraint on indices, only on values, which allows treating this as a value-based sliding window.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Building the set is $O(N)$; each element is the start of at most one sequence, and the inner `while` loop across all sequences visits each element at most once total.
- **$O(N)$ space**: The hash set stores all unique values.
- The sequence-start guard (`num - 1 not in set`) is what collapses the naive $O(N^2)$ approach into $O(N)$.

## 4. How It Works

We load all numbers into a set for $O(1)$ lookup. For each number, we skip it if `num - 1` is in the set (it's not a sequence start). Otherwise we walk forward with `num + 1`, `num + 2`, … counting the run length until we fall off the end of the sequence, then update the answer.

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

Iterating over `nums_hashset` rather than `nums` automatically deduplicates, so duplicate values in the input don't cause incorrect counts or extra work.

### Dry Run Table
Input: `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]` $\to$ set: `{0, 1, 2, 3, 4, 5, 6, 7, 8}`

| num | num-1 in set? | sequence walk | length | ans |
|---|---|---|---|---|
| 0 | -1? no $\to$ start | 1✓ $\to$ 2✓ $\to$ 3✓ $\to$ 4✓ $\to$ 5✓ $\to$ 6✓ $\to$ 7✓ $\to$ 8✓ $\to$ 9? no | 9 | 9 |
| 3 | 2? yes $\to$ skip | — | — | 9 |
| 7 | 6? yes $\to$ skip | — | — | 9 |
| others | all have num-1 in set $\to$ skip | — | — | 9 |

Result: `9`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `nums`. Traversing `nums` to build the set takes $O(N)$ time. Since we only walk a sequence when `num - 1` is not in the set, each element in the set is visited at most twice. Thus, the overall time complexity is linear.
- **Space Complexity**: $O(N)$ auxiliary space to store the unique elements of `nums` in the hash set.
