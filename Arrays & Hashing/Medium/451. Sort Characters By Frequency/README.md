# 451. Sort Characters By Frequency
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/sort-characters-by-frequency/

## 1. Algorithm Used

Bucket sort by character frequency: place each character's repeated string into a bucket indexed by its frequency, then concatenate buckets from highest to lowest.

## 2. How to Recognize the Pattern

- "sort characters by how often they appear" → rank by frequency → bucket sort on frequency.
- The maximum frequency of any character is the length of the string → bucket array of size n+1 is sufficient.
- Bucket sort avoids the O(n log n) cost of a comparison-based sort.

## 3. Why This Algorithm Fits

- O(n) time — one pass to build the Counter, one pass to fill buckets, one reverse pass to build the result.
- O(n) space — the Counter and bucket array together hold O(n) data.
- The same bucket-sort-by-frequency pattern used in Top K Frequent Elements (347) applies directly here.

## 4. How It Works

Build a `Counter` of all characters. Create a list of empty buckets indexed 0 through n. For each character and its frequency, append `char * frequency` (the character repeated frequency times) to the bucket at that index. Finally, iterate the bucket array from the end toward the front, collecting non-empty buckets, and join the result into a string.

```python
s_frequency_hashmap = Counter(s)
buckets = [[] for _ in range(len(s) + 1)]
for char, freq in s_frequency_hashmap.items():
    buckets[freq].append(char * freq)

sorted_str_arr = []
for i in range(len(buckets) - 1, -1, -1):
    sorted_str_arr.extend(buckets[i])
return "".join(sorted_str_arr)
```

Storing `char * frequency` in the bucket rather than just the character means the final join step requires no additional repetition logic — the repeated string is already pre-built at insertion time.
