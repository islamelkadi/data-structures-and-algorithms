# Sliding Window


## Table of Contents
1. [1. What It Is](#1-what-it-is)
2. [2. When to Use It — Pattern Recognition](#2-when-to-use-it--pattern-recognition)
   - [Keywords that signal this algorithm:](#keywords-that-signal-this-algorithm)
   - [Problem characteristics:](#problem-characteristics)
3. [3. Core Technique(s)](#3-core-techniques)
   - [Technique A: Fixed-Size Window](#technique-a-fixed-size-window)
   - [Technique B: Variable-Size Window (Expand/Shrink)](#technique-b-variable-size-window-expandshrink)
   - [Technique C: At-Most-K Trick (Exactly K)](#technique-c-at-most-k-trick-exactly-k)
4. [4. Decision Framework](#4-decision-framework)
5. [5. One-Pass vs Multi-Pass Reasoning](#5-one-pass-vs-multi-pass-reasoning)
6. [6. Index and Pointer Management](#6-index-and-pointer-management)
7. [7. Complexity Patterns](#7-complexity-patterns)
8. [8. Common Pitfalls](#8-common-pitfalls)

## 1. What It Is

Sliding Window is a technique for processing contiguous subarrays or substrings in O(n) time. Instead of recomputing the window from scratch on each step, you maintain a running state and update it incrementally as the window slides: add the new right element, remove the old left element. The "window" is the range `[left, right]` of indices currently under consideration.

## 2. When to Use It — Pattern Recognition

### Keywords that signal this algorithm:
- "subarray" / "substring" → contiguous range problem, sliding window candidate
- "contiguous" → explicit signal that elements must be adjacent
- "at most k" / "exactly k" / "at least k" → constraint on window content
- "longest" / "maximum length" → variable window, expand until constraint breaks
- "shortest" / "minimum length" → variable window, shrink until constraint is met
- "window of size k" / "exactly k elements" → fixed-size window
- "product less than k" / "sum equals k" → window with numeric constraint

### Problem characteristics:
- You need an optimal (longest, shortest, maximum, minimum) contiguous range
- The constraint on the window is monotonic: if a window of size w violates it, any larger window also violates it (or vice versa)
- You can efficiently update the window state when adding/removing one element
- The answer involves all elements in a range, not just a pair

## 3. Core Technique(s)

### Technique A: Fixed-Size Window

Window size `k` is given. Compute the initial window, then slide one step at a time.

```python
# Build initial window
window_sum = sum(arr[:k])
result = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i]        # add incoming element
    window_sum -= arr[i - k]    # remove outgoing element
    result = max(result, window_sum)

return result
```

Use when: "exactly k consecutive elements", "average of every window of size k", "max sum subarray of length k".

### Technique B: Variable-Size Window (Expand/Shrink)

Expand `right` unconditionally; shrink `left` when the constraint is violated; update the answer when the window is valid.

```python
left = 0
state = {}   # or a counter, sum, etc.

for right in range(len(arr)):
    # 1. Add arr[right] to window state
    state[arr[right]] = state.get(arr[right], 0) + 1

    # 2. Shrink from left while constraint is violated
    while is_violated(state):
        state[arr[left]] -= 1
        if state[arr[left]] == 0:
            del state[arr[left]]
        left += 1

    # 3. Update answer (window [left..right] is now valid)
    result = max(result, right - left + 1)

return result
```

Use when: "longest subarray with at most k distinct", "longest substring without repeating characters", "max consecutive ones with k flips".

*Optimization — Historical Max Frequency*: In problems where validity is checked using the frequency of the most frequent character `max_freq` (e.g. `window_size - max_freq <= k` in `424. Longest Repeating Character Replacement`), we do not need to decrement `max_freq` when shrinking the window. Decreasing a character's count can never increase the overall maximum frequency. Thus, `max_freq` only needs to be updated when it increases, which only happens during expansion on the right pointer. This allows us to track a running `max_freq` without re-scanning the frequency map, maintaining true O(1) operations per step.



### Technique C: At-Most-K Trick (Exactly K)

`count(exactly k) = count(at most k) - count(at most k-1)`

```python
def at_most_k(arr, k):
    left, count, result = 0, 0, 0
    freq = {}
    for right in range(len(arr)):
        freq[arr[right]] = freq.get(arr[right], 0) + 1
        if freq[arr[right]] == 1:
            count += 1
        while count > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                count -= 1
            left += 1
        result += right - left + 1
    return result

return at_most_k(arr, k) - at_most_k(arr, k - 1)
```

Use when: "subarrays with exactly k distinct integers".

## 4. Decision Framework

```
Is the window size fixed (given as k)?
├── Yes → Fixed-size window: slide and update in O(1) per step
└── No  → Variable window

    Is the constraint monotonic?
    (larger window = harder to satisfy, or easier?)
    ├── Yes → Expand right freely, shrink left when violated
    └── No  → Sliding window may not apply; consider prefix sum + hashmap

    Do you need "exactly k" subarrays?
    └── Yes → at-most-k trick: answer = f(k) - f(k-1)
```

## 5. One-Pass vs Multi-Pass Reasoning

Sliding window is inherently a **single-pass** algorithm:
- `right` moves from 0 to n-1, never backward
- `left` also only moves forward (never decreases)
- Together they make at most 2n total pointer movements → O(n)

The key insight that enables one-pass: the constraint is **monotonic**. Once a window is invalid, making it larger won't fix it (for "at most" constraints). So you never need to re-examine a left boundary you've already passed.

Multi-pass is needed only when the window state requires information from the future (rare — usually solvable with prefix sums instead).

## 6. Index and Pointer Management

- **Window size**: `right - left + 1` (inclusive on both ends)
- **Fixed window initialization**: process `arr[0..k-1]` before the loop, then loop `i` from `k` to `n-1`
- **Variable window**: `left` starts at 0 and only moves right; update answer *after* shrinking (so the window is valid when you record it)
- **Shrink condition**: use `while`, not `if` — multiple elements may need to be removed before the window is valid again
- **Answer update placement**:
  - For longest/maximum: update after shrinking (window is valid)
  - For shortest/minimum: update inside the shrink loop (each valid window before shrinking is a candidate)

## 7. Complexity Patterns

| Variant | Time | Space |
|---|---|---|
| Fixed-size window | O(n) | O(1) or O(k) |
| Variable window (no hashmap) | O(n) | O(1) |
| Variable window (with hashmap) | O(n) | O(k) where k = distinct elements |
| At-most-k trick | O(n) | O(k) |

The two-pointer movement guarantees O(n): each of the n elements is added once and removed at most once.

## 8. Common Pitfalls

- **Using `if` instead of `while` to shrink**: a single removal may not restore validity; always use `while is_violated(state)`
- **Updating answer before shrinking**: for longest-window problems, record the answer after the shrink loop, not before — otherwise you record an invalid window
- **Off-by-one in window size**: window length is `right - left + 1`, not `right - left`
- **Fixed vs variable confusion**: if the problem says "exactly k elements", it's fixed-size; if it says "at most k" or "longest satisfying condition", it's variable
- **Forgetting to clean up the hashmap**: when a frequency drops to 0, delete the key (or check `> 0`) to avoid counting zero-frequency elements as "present"
- **At-most-k trick direction**: `exactly(k) = at_most(k) - at_most(k-1)`, not `at_most(k+1) - at_most(k)`
