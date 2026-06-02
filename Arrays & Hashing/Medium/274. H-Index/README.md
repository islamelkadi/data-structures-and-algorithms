# 274. H-Index

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/h-index/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Counting Sort (distribution sorting) followed by a greedy descending scan.

## 2. How to Recognize the Pattern

- **H-Index logic**: "Find the maximum value $h$ such that the researcher has published at least $h$ papers that have each been cited at least $h$ times." This requires evaluating papers in descending order of their citations.
- **Sorting optimization**: Instead of a standard $O(N \log N)$ sort, we can count frequencies of citations and rebuild the array in-place to achieve $O(N + K)$ time, where $K$ is the maximum citation count.
- **In-place slice modification**: Using slice assignment `citations[:] = []` permits modifying the input array in-place without generating a new reference.

## 3. Why This Algorithm Fits

- A frequency array collects counts in $O(N)$ time.
- Re-populating the citations array using the frequency map sorts the citations in $O(N + K)$ time.
- Traversing the sorted citations from highest to lowest lets us find the threshold index where the citation value falls below the 1-based index (count of papers).

## 4. How It Works

1. Find the maximum citation value: `max_val = max(citations)`.
2. Initialize a frequency list `count_freq_arr` of size `max_val + 1` with 0s.
3. Record the citation frequencies: `count_freq_arr[num] += 1`.
4. Empty the input list `citations[:] = []` in-place and rebuild it in sorted order using the frequency array.
5. Reverse the rebuilt array to get citations in descending order.
6. Loop through `citations` using index `i`:
   - If `citations[i] >= i + 1`, we have at least `i + 1` papers with at least `i + 1` citations.
   - If `citations[i] < i + 1`, the condition fails, meaning our maximum H-Index is `i`. Return `i`.
7. If the loop completes successfully, return the total number of papers `len(citations)`.

```python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # # Attempt 1: O(nlog(n))
        # citations.sort(reverse=True)
        # for i in range(len(citations)):
        #     if citations[i] >= i + 1:
        #         continue
        #     else:
        #         return i
        # return len(citations)

        # Attempt 2: O(n + k)
        # Create count frequency arr using count sort algorith
        max_val = max(citations)
        count_freq_arr = [0] * (max_val + 1)
        for num in citations:
            count_freq_arr[num] += 1
        
        # Create ordered array
        citations[:] = [] # empty citations array, instead of creating a new one
        for i, count in enumerate(count_freq_arr):
            if not count:
                continue
            citations.extend([i] * count)

        citations.reverse()
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                continue  # Still valid, keep going
            else:
                return i  # Failed at position i, so h-index is i
        return len(citations)  # Never failed → all papers are valid
```

### Dry Run Table
Input: `citations = [3, 0, 6, 1, 5]`  
`max_val = 6`, `count_freq_arr = [1, 1, 0, 1, 0, 1, 1]`  
Sorted & Reversed Citations: `[6, 5, 3, 1, 0]`

| i | citations[i] | Paper Count (`i + 1`) | Condition: `citations[i] >= i + 1` | Action |
|---|--------------|----------------------|------------------------------------|--------|
| 0 | 6            | 1                    | `6 >= 1` (True)                    | continue |
| 1 | 5            | 2                    | `5 >= 2` (True)                    | continue |
| 2 | 3            | 3                    | `3 >= 3` (True)                    | continue |
| 3 | 1            | 4                    | `1 >= 4` (False)                   | return `i` = 3 |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N + K)$ where $N$ is the number of papers and $K$ is the maximum citation value. Finding the max, counting frequencies, rebuilding the array, and checking the threshold take linear time.
- **Space Complexity**: $O(K)$ auxiliary space to store the frequency array `count_freq_arr` of size $K + 1$.
