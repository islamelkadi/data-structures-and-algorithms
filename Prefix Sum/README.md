# Prefix Sum


## Table of Contents
1. [1. What It Is](#1-what-it-is)
2. [2. When to Use It — Pattern Recognition](#2-when-to-use-it--pattern-recognition)
   - [Keywords that signal this algorithm:](#keywords-that-signal-this-algorithm)
   - [Problem characteristics:](#problem-characteristics)
3. [3. Core Technique(s)](#3-core-techniques)
   - [Technique A: Basic Prefix Sum (Range Queries)](#technique-a-basic-prefix-sum-range-queries)
   - [Technique B: Prefix Sum + Hashmap (Subarray Sum = K)](#technique-b-prefix-sum--hashmap-subarray-sum--k)
   - [Technique C: Prefix + Suffix (Product Except Self)](#technique-c-prefix--suffix-product-except-self)
   - [Technique D: Pivot Index (Equal Left and Right Sum)](#technique-d-pivot-index-equal-left-and-right-sum)
   - [Technique E: 2D Prefix Sum (Submatrix Queries)](#technique-e-2d-prefix-sum-submatrix-queries)
4. [4. Decision Framework](#4-decision-framework)
5. [5. One-Pass vs Multi-Pass Reasoning](#5-one-pass-vs-multi-pass-reasoning)
6. [6. Index and Pointer Management](#6-index-and-pointer-management)
7. [7. Complexity Patterns](#7-complexity-patterns)
8. [8. When to Use Padding vs Not](#8-when-to-use-padding-vs-not)
9. [9. Common Pitfalls](#9-common-pitfalls)

## 1. What It Is

Prefix Sum is a preprocessing technique that converts an array into a cumulative sum array, enabling any range sum query to be answered in O(1) instead of O(n). The core identity is:

```
sum(i..j) = prefix[j] - prefix[i-1]
```

where `prefix[k] = arr[0] + arr[1] + ... + arr[k]`.

Combined with a hashmap, prefix sums can find subarrays whose sum equals a target in O(n) — a problem that would otherwise require O(n²) with nested loops.

## 2. When to Use It — Pattern Recognition

### Keywords that signal this algorithm:
- "range sum query" / "sum of elements from i to j" → basic prefix sum
- "subarray sum equals k" / "number of subarrays with sum k" → prefix sum + hashmap
- "running sum" / "cumulative sum" → direct prefix sum application
- "pivot index" / "equal left and right sum" → prefix sum from both sides
- "product of array except self" → prefix product + suffix product
- "binary subarrays with sum" / "nice subarrays" → prefix sum + hashmap (treat 1s as 1, odds as 1)

### Problem characteristics:
- You need the sum of a contiguous subarray repeatedly
- You need to count subarrays satisfying a sum condition
- The problem involves "balance points" where left sum equals right sum
- Brute force would recompute sums from scratch for each query → O(n²)

## 3. Core Technique(s)

### Technique A: Basic Prefix Sum (Range Queries)

Build the prefix array once; answer each query in O(1).

```python
# Build
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]

# Query: sum of arr[i..j] (0-indexed, inclusive)
def range_sum(i, j):
    return prefix[j + 1] - prefix[i]
```

The extra leading `0` (1-indexed prefix array) avoids the special case when `i = 0`.

### Technique B: Prefix Sum + Hashmap (Subarray Sum = K)

For each position, check if `prefix[j] - k` has been seen before. If so, there's a subarray ending at `j` with sum `k`.

```python
from collections import defaultdict

def subarray_sum(arr, k):
    count = 0
    prefix = 0
    seen = defaultdict(int)
    seen[0] = 1   # empty prefix has sum 0

    for x in arr:
        prefix += x
        count += seen[prefix - k]   # subarrays ending here with sum k
        seen[prefix] += 1

    return count
```

The key insight: if `prefix[j] - prefix[i] = k`, then `prefix[i] = prefix[j] - k`. So for each `j`, look up how many times `prefix[j] - k` has appeared as a prefix sum.

**Critical**: initialize `seen[0] = 1` to handle subarrays that start from index 0.

### Technique C: Prefix + Suffix (Product Except Self)

When you need a value derived from everything except the current element:

```python
n = len(arr)
result = [1] * n

# Left pass: result[i] = product of arr[0..i-1]
prefix = 1
for i in range(n):
    result[i] = prefix
    prefix *= arr[i]

# Right pass: multiply by product of arr[i+1..n-1]
suffix = 1
for i in range(n - 1, -1, -1):
    result[i] *= suffix
    suffix *= arr[i]

return result
```

### Technique D: Pivot Index (Equal Left and Right Sum)

```python
total = sum(arr)
left_sum = 0
for i, x in enumerate(arr):
    # right_sum = total - left_sum - arr[i]
    if left_sum == total - left_sum - x:
        return i
    left_sum += x
return -1
```

### Technique E: 2D Prefix Sum (Submatrix Queries)

Precompute cumulative sums across both dimensions of a 2D matrix to query any arbitrary submatrix sum in O(1) time.

```python
m, n = len(matrix), len(matrix[0])
# 1-indexed padding on top and left to eliminate boundary checks
prefix = [[0] * (n + 1) for _ in range(m + 1)]

# Pass 1: Row-wise prefix accumulation
for r in range(m):
    for c in range(n):
        prefix[r + 1][c + 1] = prefix[r + 1][c] + matrix[r][c]

# Pass 2: Column-wise prefix accumulation (summing columns down)
for c in range(1, n + 1):
    for r in range(1, m + 1):
        prefix[r][c] += prefix[r - 1][c]

# Query submatrix sum from (r1, c1) to (r2, c2) (0-indexed, inclusive)
def sumRegion(r1, c1, r2, c2):
    return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]
```

Use when: "2D grid submatrix range sums", "multiple submatrix queries on an immutable matrix".

## 4. Decision Framework

```
Do you need sum of a fixed range [i..j] in 1D?
└── Basic prefix array: O(1) per query after O(n) build

Do you need sum of an arbitrary submatrix [r1, c1] to [r2, c2] in 2D?
└── 2D prefix array (padded left/top): O(1) per query after O(m*n) build

Do you need to count subarrays with sum = k?
└── Prefix sum + hashmap: O(n) total
```

Do you need a value derived from all elements except self?
└── Prefix product + suffix product: O(n), O(1) extra space

Do you need a balance/pivot point?
└── Running left sum + total sum: O(n)

Is the array binary (0s and 1s) and you need "sum = k" subarrays?
└── Same as subarray sum = k (treat 1s as 1, 0s as 0)

Are values odd/even and you need "k odd numbers" subarrays?
└── Map odd→1, even→0, then apply subarray sum = k
```

## 5. One-Pass vs Multi-Pass Reasoning

**Basic prefix sum**: two passes — one to build the prefix array, then queries are O(1).

**Prefix sum + hashmap**: **one pass** — build the prefix sum and query the hashmap simultaneously. You don't need the full prefix array; just maintain a running sum and a frequency map of sums seen so far.

**Product except self**: two passes (left-to-right, then right-to-left) — each pass fills in half the answer.

**Pivot index**: one pass — maintain running left sum and compare against derived right sum.

The one-pass hashmap approach works because you only need to know "how many times has this prefix sum appeared before the current position" — and "before" is exactly what you've already processed.

## 6. Index and Pointer Management

- **1-indexed prefix array**: `prefix[0] = 0`, `prefix[i] = prefix[i-1] + arr[i-1]`. Range sum `arr[i..j]` (0-indexed) = `prefix[j+1] - prefix[i]`. Avoids edge cases when the subarray starts at index 0.
- **0-indexed prefix array**: `prefix[i] = arr[0] + ... + arr[i]`. Range sum `arr[i..j]` = `prefix[j] - prefix[i-1]`, with special case `prefix[j]` when `i = 0`.
- **Hashmap initialization**: always seed `seen[0] = 1` before the loop — this handles subarrays starting from index 0 (where `prefix[j] - k = 0`).
- **Running sum vs array**: for the hashmap technique, you don't need to store the full prefix array — a single running variable `prefix` is sufficient.

## 7. Complexity Patterns

| Technique | Time | Space |
|---|---|---|
| Basic prefix array (build) | O(n) | O(n) |
| Range sum query | O(1) per query | O(1) |
| Subarray sum = k (hashmap) | O(n) | O(n) |
| Product except self | O(n) | O(1) extra |
| Pivot index | O(n) | O(1) |

## 8. When to Use Padding vs Not

The need for padding comes down to whether you're doing range queries or just point lookups.

**No padding needed** — if you only need the prefix value at a single point (sum from index 0 to i), you index directly and there's no subtraction risk:

```python
prefix[i] = prefix[i-1] + nums[i]
# sum from 0 to i = prefix[i]  ← no subtraction, no boundary issue
```

**Padding is needed** — when you need arbitrary range queries `sum(l, r)`, you subtract:

```python
sum(l, r) = prefix[r] - prefix[l-1]
```

When `l = 0`, `l - 1 = -1` causes an index error. A leading 0 shifts everything right by 1, making `prefix[0] = 0` a safe sentinel:

```python
sum(l, r) = prefix[r+1] - prefix[l]  # no -1 risk, works for any l
```

Without padding you'd need an explicit guard every time:
```python
left = prefix[l - 1] if l > 0 else 0  # messy, easy to forget
```

**In 2D** the same rule applies in both dimensions — left padding covers column range queries, top padding covers row range queries. If you're querying arbitrary submatrices (like in problem 304), you need both.

| Use case | Padding? |
|---|---|
| Sum from index 0 to i | No |
| Sum from index l to r (arbitrary l) | Yes |
| 2D submatrix sum query | Yes (both dimensions) |

## 9. Common Pitfalls

- **Forgetting `seen[0] = 1`**: without this, subarrays starting at index 0 are missed — this is the most common bug in the hashmap technique
- **Off-by-one in range query**: `sum(arr[i..j])` with 0-indexed prefix array is `prefix[j] - prefix[i-1]`, which breaks when `i = 0`; use a 1-indexed prefix array to avoid this
- **Counting vs finding**: `subarray_sum` counts all subarrays with sum k; if you need to find one, store the index in the hashmap instead of the count
- **Negative numbers**: prefix sum + hashmap works correctly with negative numbers (unlike sliding window, which requires non-negative values for the monotonic property to hold)
- **Integer overflow**: in languages with fixed-size integers, prefix sums of large arrays can overflow — use 64-bit integers when needed
- **Product except self with zeros**: if the array contains zeros, the product-except-self approach still works correctly, but be careful about dividing by zero if you try to use the naive `total_product / arr[i]` shortcut
