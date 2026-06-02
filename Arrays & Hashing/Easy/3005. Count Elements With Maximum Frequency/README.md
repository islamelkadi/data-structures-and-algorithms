# 3005. Count Elements With Maximum Frequency

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/count-elements-with-maximum-frequency/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm utilizes a Hash Map (implemented via Python's `collections.Counter`) to count the frequencies of all elements in the input array. It then finds the maximum frequency among these elements and sums up the total occurrences of all elements that share this maximum frequency.

## 2. How to Recognize the Pattern

- **Frequency Counting**: The problem explicitly mentions finding elements with the "maximum frequency" and counting their total occurrences. Any question involving counting frequencies of elements is a direct indicator for using a Hash Map / Hash Table.
- **Alternatives**: Sorting the array first would allow us to count consecutive elements in $O(1)$ extra space, but it would increase the time complexity to $O(N \log N)$. Using a Hash Map allows us to do this in linear time $O(N)$ with $O(N)$ space, which is optimal.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ — We perform one pass to count the elements ($O(N)$), one pass over the frequencies to find the maximum value ($O(U)$ where $U$ is the number of unique elements), and one final pass over the frequencies to sum the maximum occurrences ($O(U)$). Since $U \le N$, the overall time complexity is linear.
- **Space Complexity**: $O(U)$ — The space is dominated by the hash map storage, which holds at most $U$ unique key-value pairs where $U$ is the number of unique elements in `nums`.

## 4. How It Works

1. Initialize a hash map `frequency` using `Counter(nums)` to store counts of each number.
2. Find the maximum frequency using `max(frequency.values())`.
3. Iterate over the values of the frequency map. If a frequency equals the maximum frequency, add it to `total_occurrence`.
4. Return `total_occurrence`.

```python
from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        max_frequency = max(frequency.values())
        
        total_occurrence = 0
        for i in frequency.values():
            if i == max_frequency:
                total_occurrence += i
        return total_occurrence
```

### Dry Run Table
Input: `nums = [1, 2, 2, 3, 1, 4]`

`frequency = {1: 2, 2: 2, 3: 1, 4: 1}`  
`max_frequency = 2`

| Step/Index | Current Freq value (`i`) | Condition (`i == max_frequency`) | `total_occurrence` | Action Taken |
|------------|--------------------------|-----------------------------------|--------------------|--------------|
| *init*     | —                        | —                                 | 0                  | Initialize Counter and compute `max_frequency = 2` |
| 1          | 2 (for key `1`)          | `2 == 2` (True)                   | 2                  | Add `i` (2) to `total_occurrence` |
| 2          | 2 (for key `2`)          | `2 == 2` (True)                   | 4                  | Add `i` (2) to `total_occurrence` |
| 3          | 1 (for key `3`)          | `1 == 2` (False)                  | 4                  | Skip |
| 4          | 1 (for key `4`)          | `1 == 2` (False)                  | 4                  | Skip |
