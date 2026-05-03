# Algorithmic Thinking

## Table of Contents

### Algorithmic Thinking Guide
1. [How to Read a Problem](#1-how-to-read-a-problem)
2. [Pattern Recognition Decision Tree](#2-pattern-recognition-decision-tree)
3. [One-Pass Reasoning](#3-one-pass-reasoning----can-this-be-solved-in-a-single-scan)
4. [Element Comparison Strategies](#4-element-comparison-strategies)
5. [Index Management](#5-index-management)
6. [Constraint-to-Algorithm Mapping](#6-constraint-to-algorithm-mapping)
7. [Complexity Estimation](#7-complexity-estimation)
8. [Interview Strategy](#8-interview-strategy)

### Study Plan
1. [Arrays & Strings](#1-arrays--strings)
2. [Hash Map / Set](#2-hash-map--set)
3. [Two Pointers](#3-two-pointers)
4. [Sliding Window](#4-sliding-window)
5. [Prefix Sum](#5-prefix-sum)
6. [Binary Search](#6-binary-search)
7. [Intervals](#7-intervals)
8. [Math & Geometry](#8-math--geometry)
9. [Bit Manipulation](#9-bit-manipulation)
10. [Stack](#10-stack)
11. [Linked List](#11-linked-list)
12. [Binary Tree](#12-binary-tree)
13. [Divide & Conquer](#13-divide--conquer)
14. [Graph](#14-graph)
15. [Heap / Priority Queue](#15-heap--priority-queue)
16. [Backtracking](#16-backtracking)
17. [Trie](#17-trie)
18. [Dynamic Programming](#18-dynamic-programming)
19. [Queue / Design](#19-queue--design)

---

My personal notes on algorithmic thinking — not a catalog of algorithms, but a framework for reasoning through problems. The goal is to go from reading a problem to knowing what to try and why.

---

## 1. How to Read a Problem

The problem statement contains everything needed — the key is knowing what to look for before writing any code.

### Read for structure, not just content

On first read, resist immediately pattern-matching to a solution. Extract the structural facts first:

- **What is the input?** Type, size, constraints (sorted? distinct? non-negative?).
- **What is the output?** A value, an index, a modified array, a boolean?
- **What is the relationship?** What transformation connects input to output?

### Annotate the constraints

Constraints are not boilerplate — they are hints. Write them down explicitly:

```
n <= 10^5       → O(n log n) or O(n) required
values distinct → no need to handle duplicates
array is sorted → binary search or two pointers are viable
k <= n          → k is bounded, can iterate over it
```

### Identify what's fixed and what varies

In sliding window problems, the window moves but the constraint stays fixed. In two-pointer problems, the pointers move but the target stays fixed. Identifying the invariant clarifies what to maintain as state.

### Restate the problem in one sentence

Before writing code, restate it as: "Given X, find Y such that Z." If that's not clean, the problem isn't fully understood yet.

### Check the examples — then construct your own

The provided examples are usually the happy path. Also check:
- Empty input
- Single element
- All elements identical
- Already sorted / reverse sorted
- Minimum and maximum values of n

---

## 2. Pattern Recognition Decision Tree

```
Is the input a linear sequence (array, string, linked list)?
│
├── YES
│   ├── Looking for a subarray or substring?
│   │   ├── Fixed length window → Sliding Window (fixed)
│   │   ├── Variable length with constraint → Sliding Window (variable)
│   │   └── Count subarrays with exact sum → Prefix Sum + HashMap
│   │
│   ├── Comparing or pairing elements?
│   │   ├── Sorted input, pair with target sum → Two Pointers (converging)
│   │   ├── Unsorted, pair/complement → HashMap
│   │   └── Subsequence / merge of two sequences → Two Pointers (same direction)
│   │
│   ├── "Next greater / previous smaller" query? → Monotonic Stack
│   ├── Running totals or range sums? → Prefix Sum
│   └── Reversals, palindromes, in-place edits? → Two Pointers
│
└── NO — Graph, tree, or grid?
    ├── Tree traversal → DFS / BFS
    ├── Shortest path → BFS (unweighted) / Dijkstra (weighted)
    └── Optimization over subproblems → Dynamic Programming
```

### Secondary signals

| Signal | Likely Pattern |
|---|---|
| "at most k", "no more than k" | Sliding window or prefix sum |
| "exactly k" | at-most(k) − at-most(k−1) trick |
| "sorted array" | Two pointers or binary search |
| "frequency", "count occurrences" | HashMap / Counter |
| "next greater element" | Monotonic stack |
| "range sum query" | Prefix sum |
| "in-place", "O(1) space" | Two pointers or bit manipulation |
| "missing number", "single non-duplicate" | XOR / bit manipulation |

---

## 3. One-Pass Reasoning — Can This Be Solved in a Single Scan?

A single pass means you iterate through the input exactly once, making all decisions as you go.

### When a single pass is sufficient

A problem is solvable in one pass when the decision at index `i` depends only on:
1. Information already seen (prefix state), or
2. A fixed invariant that doesn't require future knowledge

**Examples:**
- **Running maximum**: compare to a running max. No lookahead needed.
- **Two Sum (unsorted)**: store seen values in a hash map. When you see `target - x`, you already have `x`.
- **Valid Parentheses**: a stack tracks open brackets. Close brackets resolve immediately.
- **Sliding window**: expand right, shrink left when constraint violated. One pass.

### When a single pass is NOT sufficient

You need multiple passes when:
- The decision at `i` depends on something to the right (future state)
- You need a global property first (e.g., total sum) before making local decisions

**Example — Product of Array Except Self:**

```python
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
```

### The carry-forward test

Ask: "What state needs to carry from index `i` to index `i+1`?" If the answer is a fixed-size structure (counter, running sum, stack, hash map), a single pass is likely viable.

### One-pass with two pointers

Two pointers moving in the same direction is still one pass — both pointers together traverse the array once.

```python
# Move Zeros — one pass, two pointers
def moveZeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    while write < len(nums):
        nums[write] = 0
        write += 1
```

---

## 4. Element Comparison Strategies

How you compare elements determines your pointer setup.

### Comparing element to itself at index i

Check a property of `nums[i]` alone, possibly against a running aggregate.

```python
# Boyer-Moore majority vote
count = 0
candidate = None
for num in nums:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)
```

### Comparing to element ahead (i+1, i+2)

Look forward from the current position. Basis of fast/slow pointer and sliding window logic.

```python
# String Compression — compare chars[i] to chars[i+1]
i = 0
while i < len(chars):
    char = chars[i]
    count = 0
    while i < len(chars) and chars[i] == char:
        i += 1
        count += 1
    # write char and count...
```

**Off-by-one note:** When comparing `nums[i]` to `nums[i+1]`, the loop must stop at `len(nums) - 1`.

### Comparing to element behind (i-1)

Look backward — natural for "is this a new group?" logic.

```python
# Count distinct values in sorted array
count = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        count += 1
```

Starting at index 1 is intentional — there's no `nums[-1]` to compare against at index 0.

### Comparing from both ends

Two pointers start at opposite ends and converge.

```python
# Two Sum II — sorted array
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1
```

**Why this works on sorted arrays:** Moving `left` right strictly increases the sum; moving `right` left strictly decreases it. On an unsorted array, you have no such guarantee.

---

## 5. Index Management

Index bugs are the most common source of wrong answers on problems that are conceptually understood.

### When to start at index 0 vs 1

**Start at 0** when:
- Processing every element independently
- Using the index as a write pointer

**Start at 1** when:
- Comparing `nums[i]` to `nums[i-1]` — starting at 0 would access `nums[-1]`
- The first element has already been processed as initialization

```python
# Prefix sum — index 0 is a sentinel
prefix = [0] * (len(nums) + 1)
for i in range(len(nums)):
    prefix[i + 1] = prefix[i] + nums[i]

# Range sum [l, r] inclusive:
range_sum = prefix[r + 1] - prefix[l]
```

### Off-by-one reasoning

**Fence-post errors:** An array of `n` elements has `n-1` adjacent pairs. A loop `for i in range(n-1)` iterates over those pairs via `(nums[i], nums[i+1])`.

**Boundary inclusion errors:** When the loop condition is `while left < right`, the loop stops when `left == right` — that element is not processed. Worth checking whether that's correct for the problem.

**A reliable technique:** Trace through a 2-element or 3-element example by hand.

### Boundary conditions

- **Empty input:** Does the code handle `len(nums) == 0`? Many algorithms initialize with `nums[0]` — this crashes on empty input.
- **Single element:** A loop `for i in range(1, len(nums))` never executes on a single-element array.
- **Two-pointer termination:** `while left < right` is almost always correct. Using `<=` causes pointers to cross.

**The exclusive-right mental model:** Think of the window as `[left, right)`. Then `right - left` is always the window size, and `right == len(s)` is the natural termination condition.

---

## 6. Constraint-to-Algorithm Mapping

Reading constraints isn't just about knowing the input size — it's about ruling out entire classes of algorithms before writing a single line. The constraints are the problem setter telling you exactly what they expect.

### Input size constraints

TLE (Time Limit Exceeded) means the solution ran too slowly on LeetCode's test cases. Use `n` to estimate the maximum acceptable complexity before coding.

| Constraint | Max viable complexity | Typical algorithms |
|---|---|---|
| n ≤ 20 | O(2^n) or O(n!) | Backtracking, bitmask DP |
| n ≤ 10^2 | O(n^3) | Triple nested loops |
| n ≤ 10^3 | O(n^2) | Double nested loops, DP |
| n ≤ 10^5 | O(n log n) | Sorting, binary search |
| n ≤ 10^6 | O(n) | Single pass, hash maps, prefix sums |
| n ≤ 10^9 | O(log n) | Binary search on answer, math |

**How to use this:** multiply the complexity by `n` and check if it exceeds ~10^8 operations. If it does, the approach will TLE.

```
n = 10^5, algorithm is O(n^2) → 10^10 operations → TLE
n = 10^5, algorithm is O(n log n) → ~1.7 × 10^6 operations → fine
```

### Value constraints

Value constraints narrow down the approach independently of input size.

| Constraint | Implication |
|---|---|
| Values in [1, n] | Can use the value as an array index (index-as-hash trick) |
| Values are non-negative | Sliding window shrink condition is monotone — window sum only grows as right expands |
| Values can be negative | Sliding window may not work; adding an element can decrease the sum, breaking monotonicity. Use prefix sum + hash map instead |
| Values are distinct | No duplicate handling needed; sets and direct comparisons are safe |
| Values are bounded (e.g., lowercase letters only) | Use a fixed-size frequency array of size 26 instead of a hash map — faster and simpler |
| Values are 0 or 1 | Sliding window and prefix sum both work cleanly; bit tricks may apply |

#### The index-as-hash trick

When values are guaranteed to be in `[1, n]`, the array itself can act as a hash map by using the value as an index. This gives O(1) lookup with no extra space.

```python
# Mark visited values in-place by negating nums[abs(val) - 1]
def findDuplicates(nums):
    result = []
    for val in nums:
        idx = abs(val) - 1
        if nums[idx] < 0:
            result.append(abs(val))
        else:
            nums[idx] *= -1
    return result
```

#### Negative values break sliding windows

A sliding window works because expanding the window (moving `right`) monotonically increases the running value, and shrinking (moving `left`) monotonically decreases it. Negative numbers break this — adding a negative element can decrease the sum, so there's no longer a clean shrink condition.

```python
# This does NOT work correctly with negative values:
def maxSubarraySum(nums, k):
    left = total = 0
    for right in range(len(nums)):
        total += nums[right]
        while total > k:       # shrink condition is no longer reliable
            total -= nums[left]
            left += 1
```

Use Kadane's algorithm or prefix sum + hash map for subarrays with negative values.

### Array structure constraints

| Constraint | Implication |
|---|---|
| Array is sorted | Two pointers or binary search are viable; hash maps may be unnecessary |
| Array is rotated sorted | Modified binary search (check which half is sorted) |
| Array has a majority element | Boyer-Moore voting works in O(n) time, O(1) space |
| Array is a permutation of [1..n] | XOR or sum formula can find missing/duplicate in O(n), O(1) |
| Matrix rows and columns are sorted | Binary search per row, or staircase search from top-right corner |

### String constraints

| Constraint | Implication |
|---|---|
| Only lowercase letters | Fixed 26-size array instead of hash map |
| Anagram / permutation check | Frequency count comparison; sliding window of fixed size |
| Palindrome check | Two pointers from both ends, or expand-around-center |
| Substring search | Sliding window; for exact match use fixed-size window |

### The "exactly k" trick

Problems asking for subarrays with **exactly k** of something can't use a plain sliding window because the window can't cleanly shrink when the count hits exactly `k`. The fix:

```
count(exactly k) = count(at most k) - count(at most k-1)
```

"At most k" is a valid sliding window problem (shrink when count exceeds k). Subtracting the two gives exactly k.

```python
def subarraysWithKDistinct(nums, k):
    def at_most(k):
        count = {}
        left = result = 0
        for right, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            result += right - left + 1
        return result
    return at_most(k) - at_most(k - 1)
```

This pattern applies to: distinct integers, odd numbers, characters, 1s — anything countable.

### Graph / tree constraints

| Constraint | Implication |
|---|---|
| Unweighted graph, shortest path | BFS (guarantees fewest edges) |
| Weighted graph, shortest path | Dijkstra (non-negative weights) or Bellman-Ford (negative weights) |
| Detect cycle in directed graph | DFS with a "currently in stack" visited state |
| Detect cycle in undirected graph | Union-Find or DFS with parent tracking |
| Tree (n nodes, n-1 edges, connected) | No cycle handling needed; DFS/BFS work directly |
| Grid traversal | BFS for shortest path; DFS for connected components / flood fill |

---

## 7. Complexity Estimation

### Reading Big O from code structure

| Code structure | Complexity |
|---|---|
| Single loop over n elements | O(n) |
| Nested loops, both over n | O(n^2) |
| Loop + binary search inside | O(n log n) |
| Recursive with halving | O(n log n) or O(log n) |
| Hash map lookup/insert | O(1) amortized |
| Sorting | O(n log n) |

### The amortized argument for sliding windows

A common mistake: seeing a `while` loop inside a `for` loop and concluding O(n^2). For sliding windows, the inner loop is amortized O(1) per outer iteration.

**Why?** Each element is added to the window at most once and removed at most once. Total operations: O(n).

```python
# This is O(n), not O(n^2)
left = 0
for right in range(n):
    window.add(nums[right])
    while window_is_invalid():   # each element enters/exits at most once
        window.remove(nums[left])
        left += 1
```

### The 10^8 operations rule of thumb

A modern machine executes roughly 10^8–10^9 simple operations per second. If your algorithm does 10^10 operations for n = 10^5, it will TLE.

### When O(n^2) is acceptable

If n ≤ 1000, an O(n^2) solution is fine (10^6 operations). Don't optimize prematurely.

---

## 8. Interview Strategy

### The first 3–5 minutes: don't code yet

1. **Read the problem twice.** Once for content, once for constraints.
2. **Ask clarifying questions.** Eliminate ambiguity that would force a rewrite later.
3. **State your understanding.** e.g. "So I need to find the length of the longest subarray where the sum is at most k — is that right?"
4. **Work through the examples.** Trace the provided examples by hand. Construct one edge case.

### Clarifying questions worth asking

- "Can the input be empty?" — affects initialization
- "Can values be negative?" — affects sliding window viability
- "Is the array sorted?" — enables two pointers or binary search
- "Are values distinct?" — simplifies duplicate handling
- "What should be returned if there's no valid answer?"

### Thinking out loud

Narrate the reasoning, not the code.

**Good:** "The array is sorted, so two pointers work here instead of a hash map — that drops space from O(n) to O(1)."

**Bad:** "Writing a for loop that goes from 0 to n..."

### The solution progression

1. **Brute force first** — state it, give its complexity, explain why it's too slow.
2. **Identify the bottleneck** — "The O(n^2) comes from the inner loop. Precomputing a hash map makes that O(1)."
3. **Propose the optimized approach** — explain the key insight before coding.
4. **Code the optimized solution** — clean, readable, meaningful variable names.
5. **Test with examples** — trace through the provided example and an edge case.

### Handling edge cases

After the solution passes the main example, explicitly check:

```
□ Empty input
□ Single element
□ All elements identical
□ Already satisfies the condition (answer is the whole array)
□ No valid answer exists
□ Minimum and maximum values of n
```

### Time management

| Phase | Time budget (45-min interview) |
|---|---|
| Reading + clarifying | 3–5 min |
| Brute force + analysis | 3–5 min |
| Optimized approach discussion | 5–7 min |
| Coding | 15–20 min |
| Testing + edge cases | 5–7 min |
| Questions for interviewer | 2–3 min |

### When stuck

1. Go back to the examples. Trace them slowly.
2. Simplify the problem. What if n = 2?
3. Think about what information is needed. "To answer at index i, I need X. Can I precompute X?"
4. Name the bottleneck. "The slow part is finding Y. Is there a data structure that gives Y in O(1)?"
5. Ask for a hint rather than sitting in silence.

---

## Quick Reference

### Pattern → Algorithm

| Problem shape | Algorithm |
|---|---|
| Subarray with constraint | Sliding window |
| Pair/complement in unsorted | HashMap |
| Pair/complement in sorted | Two pointers |
| Range sum query | Prefix sum |
| Count subarrays with exact k | Prefix sum + at-most trick |
| Next greater/smaller element | Monotonic stack |
| In-place array manipulation | Two pointers (same direction) |
| Palindrome / symmetric check | Two pointers (converging) |
| Missing/unique element | XOR / bit manipulation |

### Constraint → Complexity budget

| n | Max complexity |
|---|---|
| ≤ 20 | O(2^n) |
| ≤ 10^3 | O(n^2) |
| ≤ 10^5 | O(n log n) |
| ≤ 10^6 | O(n) |
| ≤ 10^9 | O(log n) |


---

# Study Plan — LeetCode Question Tracker

Questions sourced from:
- [Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)
- [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/)
- [Top 100 Liked](https://leetcode.com/studyplan/top-100-liked/)
- [Blind 75](https://leetcode.com/problem-list/oizxjoit/)

✅ = solved (solution exists in this repo) · ⬜ = not yet solved

---

## 1. Arrays & Strings

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 26 | Remove Duplicates from Sorted Array | Easy | ⬜ |
| 27 | Remove Element | Easy | ⬜ |
| 66 | Plus One | Easy | ⬜ |
| 88 | Merge Sorted Array | Easy | ✅ |
| 118 | Pascal's Triangle | Easy | ⬜ |
| 121 | Best Time to Buy and Sell Stock | Easy | ✅ |
| 169 | Majority Element | Easy | ✅ |
| 189 | Rotate Array | Medium | ⬜ |
| 217 | Contains Duplicate | Easy | ✅ |
| 268 | Missing Number | Easy | ✅ |
| 283 | Move Zeroes | Easy | ✅ |
| 412 | Fizz Buzz | Easy | ✅ |
| 13 | Roman to Integer | Easy | ✅ |
| 14 | Longest Common Prefix | Easy | ✅ |
| 80 | Remove Duplicates from Sorted Array II | Medium | ⬜ |
| 122 | Best Time to Buy and Sell Stock II | Medium | ⬜ |
| 128 | Longest Consecutive Sequence | Medium | ✅ |
| 134 | Gas Station | Medium | ⬜ |
| 152 | Maximum Product Subarray | Medium | ✅ |
| 238 | Product of Array Except Self | Medium | ✅ |
| 334 | Increasing Triplet Subsequence | Medium | ✅ |
| 380 | Insert Delete GetRandom O(1) | Medium | ⬜ |
| 443 | String Compression | Medium | ✅ |
| 36 | Valid Sudoku | Medium | ✅ |
| 48 | Rotate Image | Medium | ⬜ |
| 49 | Group Anagrams | Medium | ✅ |
| 53 | Maximum Subarray | Medium | ⬜ |
| 55 | Jump Game | Medium | ⬜ |
| 45 | Jump Game II | Medium | ⬜ |
| 75 | Sort Colors | Medium | ⬜ |
| 31 | Next Permutation | Medium | ⬜ |
| 135 | Candy | Hard | ⬜ |
| 42 | Trapping Rain Water | Hard | ✅ |
| 239 | Sliding Window Maximum | Hard | ⬜ |

---

## 2. Hash Map / Set

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 202 | Happy Number | Easy | ✅ |
| 205 | Isomorphic Strings | Easy | ✅ |
| 242 | Valid Anagram | Easy | ✅ |
| 290 | Word Pattern | Easy | ✅ |
| 383 | Ransom Note | Easy | ✅ |
| 1207 | Unique Number of Occurrences | Easy | ✅ |
| 2215 | Find the Difference of Two Arrays | Easy | ✅ |
| 271 | Encode and Decode Strings | Medium | ✅ |
| 347 | Top K Frequent Elements | Medium | ✅ |
| 451 | Sort Characters By Frequency | Medium | ✅ |
| 791 | Custom Sort String | Medium | ✅ |
| 1657 | Determine if Two Strings Are Close | Medium | ✅ |
| 2225 | Find Players With Zero or One Losses | Medium | ✅ |
| 2352 | Equal Row and Column Pairs | Medium | ✅ |

---

## 3. Two Pointers

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 125 | Valid Palindrome | Easy | ✅ |
| 344 | Reverse String | Easy | ✅ |
| 345 | Reverse Vowels of a String | Easy | ✅ |
| 392 | Is Subsequence | Easy | ✅ |
| 557 | Reverse Words in a String III | Easy | ✅ |
| 2540 | Minimum Common Value | Easy | ✅ |
| 11 | Container With Most Water | Medium | ✅ |
| 15 | 3Sum | Medium | ✅ |
| 151 | Reverse Words in a String | Medium | ✅ |
| 167 | Two Sum II - Input Array Is Sorted | Medium | ✅ |
| 1679 | Max Number of K-Sum Pairs | Medium | ✅ |

---

## 4. Sliding Window

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 219 | Contains Duplicate II | Easy | ✅ |
| 485 | Max Consecutive Ones | Easy | ✅ |
| 1446 | Consecutive Characters | Easy | ✅ |
| 3 | Longest Substring Without Repeating Characters | Medium | ✅ |
| 209 | Minimum Size Subarray Sum | Medium | ✅ |
| 340 | Longest Substring with At Most K Distinct Characters | Medium | ✅ |
| 424 | Longest Repeating Character Replacement | Medium | ✅ |
| 438 | Find All Anagrams in a String | Medium | ⬜ |
| 487 | Max Consecutive Ones II | Medium | ✅ |
| 567 | Permutation in String | Medium | ✅ |
| 713 | Subarray Product Less Than K | Medium | ✅ |
| 1004 | Max Consecutive Ones III | Medium | ✅ |
| 1208 | Get Equal Substrings Within Budget | Medium | ✅ |
| 1493 | Longest Subarray of 1s After Deleting One Element | Medium | ✅ |
| 1695 | Maximum Erasure Value | Medium | ✅ |
| 2958 | Length of Longest Subarray With at Most K Frequency | Medium | ✅ |
| 76 | Minimum Window Substring | Hard | ✅ |
| 992 | Subarrays with K Different Integers | Hard | ✅ |
| 2962 | Count Subarrays Where Max Element Appears at Least K Times | Hard | ✅ |

---

## 5. Prefix Sum

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 303 | Range Sum Query - Immutable | Easy | ✅ |
| 724 | Find Pivot Index | Easy | ✅ |
| 1413 | Minimum Value to Get Positive Step by Step Sum | Easy | ✅ |
| 1480 | Running Sum of 1d Array | Easy | ✅ |
| 1732 | Find the Highest Altitude | Easy | ✅ |
| 1991 | Find the Middle Index in Array | Easy | ✅ |
| 304 | Range Sum Query 2D - Immutable | Medium | ⬜ |
| 325 | Maximum Size Subarray Sum Equals k | Medium | ✅ |
| 560 | Subarray Sum Equals K | Medium | ✅ |
| 930 | Binary Subarrays with Sum | Medium | ✅ |
| 1248 | Count Number of Nice Subarrays | Medium | ✅ |

---

## 6. Binary Search

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 35 | Search Insert Position | Easy | ⬜ |
| 374 | Guess Number Higher or Lower | Easy | ⬜ |
| 33 | Search in Rotated Sorted Array | Medium | ⬜ |
| 34 | Find First and Last Position of Element in Sorted Array | Medium | ⬜ |
| 74 | Search a 2D Matrix | Medium | ⬜ |
| 153 | Find Minimum in Rotated Sorted Array | Medium | ⬜ |
| 162 | Find Peak Element | Medium | ⬜ |
| 240 | Search a 2D Matrix II | Medium | ⬜ |
| 875 | Koko Eating Bananas | Medium | ⬜ |
| 2300 | Successful Pairs of Spells and Potions | Medium | ⬜ |
| 4 | Median of Two Sorted Arrays | Hard | ⬜ |

---

## 7. Intervals

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 228 | Summary Ranges | Easy | ⬜ |
| 252 | Meeting Rooms | Easy | ⬜ |
| 56 | Merge Intervals | Medium | ⬜ |
| 57 | Insert Interval | Medium | ⬜ |
| 253 | Meeting Rooms II | Medium | ⬜ |
| 435 | Non-overlapping Intervals | Medium | ⬜ |
| 452 | Minimum Number of Arrows to Burst Balloons | Medium | ⬜ |

---

## 8. Math & Geometry

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 9 | Palindrome Number | Easy | ⬜ |
| 67 | Add Binary | Easy | ⬜ |
| 69 | Sqrt(x) | Easy | ⬜ |
| 168 | Excel Sheet Column Title | Easy | ⬜ |
| 171 | Excel Sheet Column Number | Easy | ⬜ |
| 258 | Add Digits | Easy | ⬜ |
| 263 | Ugly Number | Easy | ⬜ |
| 292 | Nim Game | Easy | ⬜ |
| 326 | Power of Three | Easy | ⬜ |
| 43 | Multiply Strings | Medium | ⬜ |
| 48 | Rotate Image | Medium | ⬜ |
| 50 | Pow(x, n) | Medium | ⬜ |
| 54 | Spiral Matrix | Medium | ⬜ |
| 59 | Spiral Matrix II | Medium | ⬜ |
| 73 | Set Matrix Zeroes | Medium | ⬜ |
| 172 | Factorial Trailing Zeroes | Medium | ⬜ |
| 204 | Count Primes | Medium | ⬜ |
| 149 | Max Points on a Line | Hard | ⬜ |

---

## 9. Bit Manipulation

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 136 | Single Number | Easy | ⬜ |
| 190 | Reverse Bits | Easy | ⬜ |
| 191 | Number of 1 Bits | Easy | ⬜ |
| 231 | Power of Two | Easy | ⬜ |
| 268 | Missing Number | Easy | ✅ |
| 338 | Counting Bits | Easy | ⬜ |
| 371 | Sum of Two Integers | Medium | ⬜ |
| 1318 | Minimum Flips to Make a OR b Equal to c | Medium | ⬜ |

---

## 10. Stack

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 20 | Valid Parentheses | Easy | ✅ |
| 844 | Backspace String Compare | Easy | ✅ |
| 1047 | Remove All Adjacent Duplicates In String | Easy | ✅ |
| 1544 | Make The String Great | Easy | ✅ |
| 71 | Simplify Path | Medium | ✅ |
| 150 | Evaluate Reverse Polish Notation | Medium | ✅ |
| 155 | Min Stack | Medium | ✅ |
| 394 | Decode String | Medium | ✅ |
| 739 | Daily Temperatures | Medium | ✅ |
| 853 | Car Fleet | Medium | ✅ |
| 2390 | Removing Stars From a String | Medium | ✅ |
| 84 | Largest Rectangle in Histogram | Hard | ✅ |
| 224 | Basic Calculator | Hard | ⬜ |

---

## 11. Linked List

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 21 | Merge Two Sorted Lists | Easy | ⬜ |
| 83 | Remove Duplicates from Sorted List | Easy | ✅ |
| 141 | Linked List Cycle | Easy | ⬜ |
| 160 | Intersection of Two Linked Lists | Easy | ⬜ |
| 206 | Reverse Linked List | Easy | ✅ |
| 234 | Palindrome Linked List | Easy | ⬜ |
| 876 | Middle of the Linked List | Easy | ✅ |
| 2 | Add Two Numbers | Medium | ⬜ |
| 19 | Remove Nth Node From End of List | Medium | ⬜ |
| 24 | Swap Nodes in Pairs | Medium | ⬜ |
| 61 | Rotate List | Medium | ⬜ |
| 82 | Remove Duplicates from Sorted List II | Medium | ⬜ |
| 86 | Partition List | Medium | ⬜ |
| 92 | Reverse Linked List II | Medium | ⬜ |
| 138 | Copy List with Random Pointer | Medium | ⬜ |
| 142 | Linked List Cycle II | Medium | ⬜ |
| 143 | Reorder List | Medium | ⬜ |
| 146 | LRU Cache | Medium | ⬜ |
| 148 | Sort List | Medium | ⬜ |
| 328 | Odd Even Linked List | Medium | ⬜ |
| 2095 | Delete the Middle Node of a Linked List | Medium | ⬜ |
| 2130 | Maximum Twin Sum of a Linked List | Medium | ⬜ |
| 23 | Merge k Sorted Lists | Hard | ⬜ |
| 25 | Reverse Nodes in k-Group | Hard | ⬜ |

---

## 12. Binary Tree

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 94 | Binary Tree Inorder Traversal | Easy | ⬜ |
| 100 | Same Tree | Easy | ⬜ |
| 101 | Symmetric Tree | Easy | ⬜ |
| 104 | Maximum Depth of Binary Tree | Easy | ⬜ |
| 112 | Path Sum | Easy | ⬜ |
| 226 | Invert Binary Tree | Easy | ⬜ |
| 543 | Diameter of Binary Tree | Easy | ⬜ |
| 572 | Subtree of Another Tree | Easy | ⬜ |
| 617 | Merge Two Binary Trees | Easy | ⬜ |
| 700 | Search in a Binary Search Tree | Easy | ⬜ |
| 872 | Leaf-Similar Trees | Easy | ⬜ |
| 96 | Unique Binary Search Trees | Medium | ⬜ |
| 98 | Validate Binary Search Tree | Medium | ⬜ |
| 102 | Binary Tree Level Order Traversal | Medium | ⬜ |
| 105 | Construct Binary Tree from Preorder and Inorder Traversal | Medium | ⬜ |
| 106 | Construct Binary Tree from Inorder and Postorder Traversal | Medium | ⬜ |
| 114 | Flatten Binary Tree to Linked List | Medium | ⬜ |
| 116 | Populating Next Right Pointers in Each Node II | Medium | ⬜ |
| 199 | Binary Tree Right Side View | Medium | ⬜ |
| 230 | Kth Smallest Element in a BST | Medium | ⬜ |
| 236 | Lowest Common Ancestor of a Binary Tree | Medium | ⬜ |
| 337 | House Robber III | Medium | ⬜ |
| 450 | Delete Node in a BST | Medium | ⬜ |
| 538 | Convert BST to Greater Tree | Medium | ⬜ |
| 1161 | Maximum Level Sum of a Binary Tree | Medium | ⬜ |
| 1372 | Longest ZigZag Path in a Binary Tree | Medium | ⬜ |
| 1448 | Count Good Nodes in Binary Tree | Medium | ⬜ |
| 107 | Binary Tree Level Order Traversal II | Medium | ⬜ |
| 124 | Binary Tree Maximum Path Sum | Hard | ⬜ |
| 297 | Serialize and Deserialize Binary Tree | Hard | ⬜ |

---

## 13. Divide & Conquer

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 108 | Convert Sorted Array to Binary Search Tree | Easy | ⬜ |
| 427 | Construct Quad Tree | Medium | ⬜ |
| 148 | Sort List | Medium | ⬜ |
| 4 | Median of Two Sorted Arrays | Hard | ⬜ |

---

## 14. Graph

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 200 | Number of Islands | Medium | ⬜ |
| 695 | Max Area of Island | Medium | ⬜ |
| 133 | Clone Graph | Medium | ⬜ |
| 130 | Surrounded Regions | Medium | ⬜ |
| 207 | Course Schedule | Medium | ⬜ |
| 210 | Course Schedule II | Medium | ⬜ |
| 261 | Graph Valid Tree | Medium | ⬜ |
| 323 | Number of Connected Components in an Undirected Graph | Medium | ⬜ |
| 399 | Evaluate Division | Medium | ⬜ |
| 417 | Pacific Atlantic Water Flow | Medium | ⬜ |
| 547 | Number of Provinces | Medium | ⬜ |
| 684 | Redundant Connection | Medium | ⬜ |
| 743 | Network Delay Time | Medium | ⬜ |
| 841 | Keys and Rooms | Medium | ⬜ |
| 994 | Rotting Oranges | Medium | ⬜ |
| 1466 | Reorder Routes to Make All Paths Lead to the City Zero | Medium | ⬜ |
| 1926 | Nearest Exit from Entrance in Maze | Medium | ⬜ |
| 79 | Word Search | Medium | ⬜ |
| 269 | Alien Dictionary | Hard | ⬜ |

---

## 15. Heap / Priority Queue

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 703 | Kth Largest Element in a Stream | Easy | ⬜ |
| 1046 | Last Stone Weight | Easy | ⬜ |
| 215 | Kth Largest Element in an Array | Medium | ⬜ |
| 253 | Meeting Rooms II | Medium | ⬜ |
| 373 | Find K Pairs with Smallest Sums | Medium | ⬜ |
| 378 | Kth Smallest Element in a Sorted Matrix | Medium | ⬜ |
| 406 | Queue Reconstruction by Height | Medium | ⬜ |
| 621 | Task Scheduler | Medium | ⬜ |
| 973 | K Closest Points to Origin | Medium | ⬜ |
| 2336 | Smallest Number in Infinite Set | Medium | ⬜ |
| 2462 | Total Cost to Hire K Workers | Medium | ⬜ |
| 2542 | Maximum Subsequence Score | Medium | ⬜ |
| 295 | Find Median from Data Stream | Hard | ⬜ |

---

## 16. Backtracking

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 17 | Letter Combinations of a Phone Number | Medium | ⬜ |
| 22 | Generate Parentheses | Medium | ⬜ |
| 39 | Combination Sum | Medium | ⬜ |
| 40 | Combination Sum II | Medium | ⬜ |
| 46 | Permutations | Medium | ⬜ |
| 78 | Subsets | Medium | ⬜ |
| 79 | Word Search | Medium | ⬜ |
| 90 | Subsets II | Medium | ⬜ |
| 131 | Palindrome Partitioning | Medium | ⬜ |
| 216 | Combination Sum III | Medium | ⬜ |
| 51 | N-Queens | Hard | ⬜ |
| 52 | N-Queens II | Hard | ⬜ |

---

## 17. Trie

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 208 | Implement Trie (Prefix Tree) | Medium | ⬜ |
| 211 | Design Add and Search Words Data Structure | Medium | ⬜ |
| 1268 | Search Suggestions System | Medium | ⬜ |
| 212 | Word Search II | Hard | ⬜ |

---

## 18. Dynamic Programming

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 70 | Climbing Stairs | Easy | ⬜ |
| 118 | Pascal's Triangle | Easy | ⬜ |
| 338 | Counting Bits | Easy | ⬜ |
| 746 | Min Cost Climbing Stairs | Easy | ⬜ |
| 1137 | N-th Tribonacci Number | Easy | ⬜ |
| 5 | Longest Palindromic Substring | Medium | ⬜ |
| 62 | Unique Paths | Medium | ⬜ |
| 64 | Minimum Path Sum | Medium | ⬜ |
| 72 | Edit Distance | Medium | ⬜ |
| 91 | Decode Ways | Medium | ⬜ |
| 97 | Interleaving String | Medium | ⬜ |
| 139 | Word Break | Medium | ⬜ |
| 198 | House Robber | Medium | ⬜ |
| 213 | House Robber II | Medium | ⬜ |
| 221 | Maximal Square | Medium | ⬜ |
| 279 | Perfect Squares | Medium | ⬜ |
| 300 | Longest Increasing Subsequence | Medium | ⬜ |
| 309 | Best Time to Buy and Sell Stock with Cooldown | Medium | ⬜ |
| 322 | Coin Change | Medium | ⬜ |
| 377 | Combination Sum IV | Medium | ⬜ |
| 416 | Partition Equal Subset Sum | Medium | ⬜ |
| 494 | Target Sum | Medium | ⬜ |
| 516 | Longest Palindromic Subsequence | Medium | ⬜ |
| 647 | Palindromic Substrings | Medium | ⬜ |
| 714 | Best Time to Buy and Sell Stock with Transaction Fee | Medium | ⬜ |
| 790 | Domino and Tromino Tiling | Medium | ⬜ |
| 1143 | Longest Common Subsequence | Medium | ⬜ |
| 85 | Maximal Rectangle | Hard | ⬜ |
| 115 | Distinct Subsequences | Hard | ⬜ |
| 312 | Burst Balloons | Hard | ⬜ |

---

## 19. Queue / Design

| # | Title | Difficulty | Solved |
|---|-------|------------|--------|
| 232 | Implement Queue using Stacks | Easy | ⬜ |
| 933 | Number of Recent Calls | Easy | ⬜ |
| 341 | Flatten Nested List Iterator | Medium | ⬜ |
| 380 | Insert Delete GetRandom O(1) | Medium | ⬜ |
| 622 | Design Circular Queue | Medium | ⬜ |
| 649 | Dota2 Senate | Medium | ⬜ |
| 295 | Find Median from Data Stream | Hard | ⬜ |
