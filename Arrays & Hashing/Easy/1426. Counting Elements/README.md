# 1426. Counting Elements
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/counting-elements/

## 1. Algorithm Used

Set membership check — count elements x where x+1 also exists in the array.

## 2. How to Recognize the Pattern

- "count elements satisfying a condition based on another element's presence" → build a lookup set → iterate and check.
- Converting to a set first turns the inner lookup from O(n) to O(1).

## 3. Why This Algorithm Fits

- O(n) time — one pass to build the set, one pass to count.
- O(n) space — the set stores all unique values.
- The set enables constant-time existence checks for x+1.

## 4. How It Works

Build a set of all values in the array. Then iterate through the array and count each element x where x+1 is present in the set.

```python
from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        return sum(1 for x in arr if x + 1 in s)
```

Note that we iterate over `arr` (not the set), so duplicates are counted individually — an element x appearing three times contributes 3 to the count if x+1 exists.
