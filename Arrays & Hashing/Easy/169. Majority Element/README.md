# 169. Majority Element
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/majority-element/

## 1. Algorithm Used

Boyer-Moore Voting Algorithm — linear time, O(1) space majority element detection.

## 2. How to Recognize the Pattern

- "element appears more than n/2 times" → majority element guaranteed to exist → Boyer-Moore.
- The guarantee that a majority element exists is what makes the voting approach correct.
- O(1) space requirement rules out a frequency map.

## 3. Why This Algorithm Fits

- O(n) time — single pass through the array.
- O(1) space — only two variables: candidate and count.
- The majority element's count can never be fully cancelled out by minority elements.

## 4. How It Works

Maintain a candidate and a vote count. When count hits 0, adopt the current element as the new candidate. Increment count for a match, decrement for a mismatch. The majority element always survives as the final candidate.

```python
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
```

Because the majority element appears more than n/2 times, it accumulates more votes than all other elements combined, so it always ends up as the surviving candidate.
