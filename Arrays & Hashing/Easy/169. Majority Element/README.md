# 169. Majority Element

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/majority-element/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Boyer-Moore Voting Algorithm — linear time, $O(1)$ space majority element detection.

## 2. How to Recognize the Pattern

- **Find an element that dominates the array**: "element appears more than n/2 times" is the classic definition of a majority element.
- **Strict O(1) space constraint**: If the problem requires finding the majority element in $O(N)$ time but $O(1)$ space (ruling out frequency maps or sorting), the Boyer-Moore Voting Algorithm is the standard approach.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Only a single pass over the input array is required.
- **$O(1)$ space**: Requires only two variables (`candidate` and `vote`), making it extremely space efficient.
- **Guaranteed majority**: Since the majority element appears more than $n/2$ times, even if all other elements "vote" against it, they cannot fully cancel out its votes.

## 4. How It Works

We maintain a `candidate` and a `vote` counter. For each element in the array:
1. If the `vote` counter is `0`, we assign the current element as the new `candidate`.
2. If the current element is equal to the `candidate`, we increment `vote`.
3. If it is different, we decrement `vote`.

Because the majority element occurs more than half the time, it is guaranteed to be the surviving candidate at the end of the pass.

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Approach 1
        # candidate, vote = nums[0], 1
        # for i in range(1, len(nums)):
        #     if nums[i] == candidate:
        #         vote += 1
        #     else:
        #         vote -= 1
            
        #     if not vote:
        #         candidate = nums[i]
        #         vote = 1
        # return candidate

        # Approach 2 - more elegant
        candidate = vote = 0
        for num in nums:
            if vote == 0:
                candidate = num
            vote += 1 if candidate == num else -1
        return candidate
```

### Dry Run Table
Input: `nums = [2, 2, 1, 1, 1, 2, 2]`

| num | vote (before check) | candidate | vote (after update) | action |
|---|---|---|---|---|
| 2 | 0 | 2 | 1 | `vote == 0` $\to$ `candidate = 2`. Match $\to$ `vote` becomes 1 |
| 2 | 1 | 2 | 2 | Match $\to$ `vote` becomes 2 |
| 1 | 2 | 2 | 1 | Mismatch $\to$ `vote` becomes 1 |
| 1 | 1 | 2 | 0 | Mismatch $\to$ `vote` becomes 0 |
| 1 | 0 | 1 | 1 | `vote == 0` $\to$ `candidate = 1`. Match $\to$ `vote` becomes 1 |
| 2 | 1 | 1 | 0 | Mismatch $\to$ `vote` becomes 0 |
| 2 | 0 | 2 | 1 | `vote == 0` $\to$ `candidate = 2`. Match $\to$ `vote` becomes 1 |

Result: `2`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of `nums`. We perform a single traversal of the array.
- **Space Complexity**: $O(1)$ as we only maintain two variables (`candidate` and `vote`) regardless of the size of the array.
