# 347. Top K Frequent Elements
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/top-k-frequent-elements/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Bucket sort by frequency: place each number into a bucket indexed by its frequency, then collect elements from the highest-frequency buckets down until k elements are gathered.

## 2. How to Recognize the Pattern

- "return the k most frequent elements" → rank by frequency → bucket sort on frequency.
- The maximum possible frequency is n (all elements the same) → bucket array of size n+1 is sufficient.
- Bucket sort avoids the O(n log n) cost of a heap or sort-based approach.

## 3. Why This Algorithm Fits

- O(n) time — one pass to build the Counter, one pass to fill buckets, one reverse pass to collect results.
- O(n) space — the Counter and bucket array each hold at most n entries.
- Bucket sort is strictly better than a heap (O(n log k)) when k is not much smaller than n.

## 4. How It Works

Build a `Counter` of all elements. Create a list of empty buckets indexed 0 through n (where index i holds all numbers that appear exactly i times). Populate the buckets using each number's frequency as its index. Finally, iterate the bucket array from the end (highest frequency) toward the front, extending the output list until it contains k elements.

```python
nums_frequency = Counter(nums)
buckets = [[] for _ in range(len(nums) + 1)]
for num, freq in nums_frequency.items():
    buckets[freq].append(num)

output = []
for i in range(len(buckets) - 1, -1, -1):
    output.extend(buckets[i])
    if len(output) >= k:
        return output
```

Using frequency as the bucket index is the core trick: it maps the ranking problem directly onto array positions, eliminating any need for comparison-based sorting.

Input: `nums = [1,1,1,2,2,3]`, `k = 2`

| step | freq | buckets (index=frequency) | output |
|------|------|--------------------------|--------|
| count | {1:3, 2:2, 3:1} | | |
| fill | | [[], [], [3], [2], [], [1], []] (size 7) | |
| collect from end | | i=6→[], i=5→[1], i=4→[], i=3→[2] | [1,2] → len>=k=2 → return |
