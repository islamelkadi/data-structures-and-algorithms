# Two Pointers


## Table of Contents
1. [1. What It Is](#1-what-it-is)
2. [2. When to Use It — Pattern Recognition](#2-when-to-use-it--pattern-recognition)
   - [Keywords that signal this algorithm:](#keywords-that-signal-this-algorithm)
   - [Problem characteristics:](#problem-characteristics)
3. [3. Core Technique(s)](#3-core-techniques)
   - [Technique A: Opposite Direction (Converging)](#technique-a-opposite-direction-converging)
   - [Technique B: Same Direction (Fast/Slow or Read/Write)](#technique-b-same-direction-fastslow-or-readwrite)
   - [Technique C: Two Arrays (Merge / Subsequence)](#technique-c-two-arrays-merge--subsequence)
4. [4. Decision Framework](#4-decision-framework)
5. [5. One-Pass vs Multi-Pass Reasoning](#5-one-pass-vs-multi-pass-reasoning)
6. [6. Index and Pointer Management](#6-index-and-pointer-management)
7. [7. Complexity Patterns](#7-complexity-patterns)
8. [8. Common Pitfalls](#8-common-pitfalls)

## 1. What It Is

Two Pointers is a technique where you maintain two index variables that move through a sequence — either toward each other from opposite ends, or in the same direction at different speeds. It turns problems that would naively require nested loops (O(n²)) into a single linear pass (O(n)).

## 2. When to Use It — Pattern Recognition

### Keywords that signal this algorithm:
- "sorted array" → opposite-direction pointers, converge toward target
- "pair sum" / "two numbers that add to k" → converge from both ends
- "palindrome" → compare characters from outside in
- "in-place" / "remove duplicates" / "move zeros" → read/write same-direction
- "subsequence" / "is subsequence" → same-direction, advance independently
- "reverse" / "swap" → opposite-direction, swap and converge

### Problem characteristics:
- Input is sorted (or can be sorted without losing information)
- You need to find a pair, triplet, or partition satisfying a condition
- You need to modify an array in-place without extra space
- You're comparing elements from both ends of a sequence
- You need to match elements of one sequence against another

## 3. Core Technique(s)

Problems are organized into three subfolders matching these techniques:
- `Opposite/` — converging pointers from both ends
- `Read & Write/` — fast/slow same-direction pointers
- `Two Arrays/` — one pointer per sequence

### Technique A: Opposite Direction (Converging)

Start `left = 0`, `right = len(arr) - 1`. Move them toward each other based on a comparison.

```python
left, right = 0, len(arr) - 1
while left < right:
    current = arr[left] + arr[right]
    if current == target:
        return [left, right]
    elif current < target:
        left += 1
    else:
        right -= 1
```

Use when: sorted array, pair sum, palindrome check, container problems.

### Technique B: Same Direction (Fast/Slow or Read/Write)

Both pointers start at the beginning. One advances unconditionally (reader), the other advances only when a condition is met (writer).

```python
write = 0
for read in range(len(arr)):
    if arr[read] != val:   # condition to keep
        arr[write] = arr[read]
        write += 1
return write
```

Use when: in-place partition, remove duplicates, move zeros, string compression.

### Technique C: Two Arrays (Merge / Subsequence)

One pointer per array, advance the one that's "behind" or matched.

```python
i, j = 0, 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1   # matched a character of s
    j += 1       # always advance through t
return i == len(s)
```

Use when: is-subsequence, merge sorted arrays, minimum common value.

## 4. Decision Framework

```
Is the array sorted (or can you sort it)?
├── Yes → Opposite-direction converging pointers
│         (pair sum, palindrome, container, 3Sum outer loop + inner converge)
└── No  → Same-direction read/write
          (partition, remove duplicates, move zeros, compress)

Do you have two separate sequences to compare?
└── Yes → Two independent pointers, one per sequence
          (is subsequence, merge sorted array, minimum common value)
```

For 3Sum: fix one element with an outer loop, then run opposite-direction on the remaining subarray.

## 5. One-Pass vs Multi-Pass Reasoning

Most two-pointer problems are solved in a **single pass** because:
- The sorted property guarantees that once you've passed a position, you don't need to revisit it
- Each pointer moves monotonically in one direction — left only increases, right only decreases
- The invariant at each step eliminates half the remaining search space

Multi-pass is needed when: you need a first pass to compute something (e.g., total sum, length) before the second pass can make decisions. Example: finding the element that appears more than n/2 times requires knowing n first.

## 6. Index and Pointer Management

- **Opposite direction**: initialize `left = 0`, `right = len - 1`; loop condition is `left < right` (not `<=`, to avoid comparing an element with itself)
- **Same direction read/write**: `write` starts at 0; `read` iterates with `for read in range(len)`; final answer is often the `write` index value
- **3Sum**: outer loop runs `i` from 0 to `len - 2`; inner pointers are `left = i + 1`, `right = len - 1`; skip duplicates by checking `arr[i] == arr[i-1]`
- **Merge from back**: when merging into the larger array (88. Merge Sorted Array), start both read pointers at the end and write from the back to avoid overwriting unread values
- **Bottleneck-driven movement**: in problems where the capacity/metric at a pointer is determined by the minimum boundary from both ends (e.g. `42. Trapping Rain Water`), update the running maxes `max_left` and `max_right`. Since the smaller boundary is the true bottleneck, calculate the trapped amount at that pointer and move it inward (increment `left` if `max_left < max_right`, otherwise decrement `right`). We do not need to know the heights of obstacles in between because the larger boundary does not limit the volume.

## 7. Complexity Patterns

| Variant | Time | Space |
|---|---|---|
| Opposite direction (sorted) | O(n) | O(1) |
| Same direction read/write | O(n) | O(1) |
| Two-array traversal | O(n + m) | O(1) |
| 3Sum (sort + two pointers) | O(n²) | O(1) or O(n) for output |

Sorting first costs O(n log n) but the pointer scan is still O(n), so the overall complexity is O(n log n) when sorting is required.

## 8. Common Pitfalls

- **Off-by-one on loop condition**: use `left < right`, not `left <= right`, for opposite-direction — otherwise you compare an element with itself
- **Skipping duplicates in 3Sum**: after finding a valid triplet, advance both pointers past all duplicates before continuing; also skip duplicate values for the outer `i` loop
- **Overwriting in merge**: when merging two sorted arrays into one of them, always fill from the back to avoid clobbering values you haven't read yet
- **Subsequence vs substring**: two pointers work for subsequence (characters don't need to be contiguous); sliding window is needed for substring/subarray problems
- **Forgetting to advance both pointers**: when a match is found in subsequence problems, only the subsequence pointer advances — the text pointer always advances
