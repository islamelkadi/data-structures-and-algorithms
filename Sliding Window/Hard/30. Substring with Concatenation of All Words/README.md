# 30. Substring with Concatenation of All Words

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Sliding window with hash-map frequency matching, run once per word-length alignment.

## 2. How to Recognize the Pattern

- **Find substrings matching a multiset of words**: Fixed-size window + frequency counter.
- **Equal-length words**: All words have equal length `w` $\to$ the string partitions into a grid of `w`-sized chunks, but the grid depends on the starting offset.
- **Multiple offsets**: Any valid concatenation's word boundaries are all congruent modulo `w`. There are exactly `w` such alignments (offsets `0, 1, ..., w-1`), so the sliding window must be run `w` times with independent state.
- **Overcount signal**: `curr[word] > need[word]` means the window is invalid and must shrink by whole words from the left.

## 3. Why This Algorithm Fits

- Brute force is $O(N \cdot K \cdot W)$. Sliding window amortizes the work: shifting forward by one word only changes the counter by $\pm 1$ entry, so `left` never moves backward within an alignment.
- Per alignment: amortized $O(1)$ shrink steps per outer step $\to$ approximately $O(N)$ work dominated by string slicing.
- All `w` alignments together: $O(N \cdot W)$ total. This is much better than brute force when `k` (number of words) is large.
- Cannot collapse into a single loop — each alignment needs its own `left` and `curr`, so state cannot be shared.

## 4. How It Works

Two nested loops:
- **Outer loop** picks the alignment offset `start` in range `[0, w)`. Each iteration resets `left = start` and `curr = {}` because alignments are independent.
- **Inner loop** slides a window forward by whole words on that alignment's grid. `i` is the window's right edge (exclusive), so the newest word is `s[i - w : i]`. After adding, if `curr[word] > need[word]`, shrink from the left one word at a time until the overcount clears. When `curr == need`, record `left`.

Three easy-to-miss details:
- `left = start`, not `0` — the left edge of the window lives on this alignment's grid.
- Inner loop range `range(start, len(s) + 1, w)` — stop at `len(s) + 1` so `i` can reach `len(s)` (since `range` is exclusive), allowing the final slice `s[len(s) - w : len(s)]`.
- Guard `if not window or len(window) < window_size: continue` — the first `i` of each alignment gives a degenerate slice (`s[start - w : start]` with negative start is empty); the guard skips any slice that isn't a full word.

```python
from collections import Counter, defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        window_size = len(words[0])
        concated_words_freq = Counter(words)

        for start in range(window_size):
            left, curr = start, defaultdict(int)
            for i in range(start, len(s) + 1, window_size):
                window = s[i - window_size : i]

                # If empty string or string on start or end
                # not valid window size, ignore and move to
                # next iteration
                if not window or len(window) < window_size:
                    continue

                # Add to window
                curr[window] += 1

                # Criteria to shrink window (a.k.a constraining criteria):
                    # C1 - If combo not in concated_words_freq
                    # C2 - If curr[combo] > concated_words_freq[s[right]]
                while curr.get(window, 0) > concated_words_freq.get(window, 0):
                    left_window = s[left: left + window_size]
                    curr[left_window] -= 1
                    if curr[left_window] == 0:
                        del curr[left_window]
                    left += window_size

                if curr == concated_words_freq:
                    ans.append(left)

        return ans
```

---

## 5. Time & Space Complexity

Let $N = \text{len}(s)$, $W = \text{len}(words[0])$, $K = \text{len}(words)$.

- **Time Complexity**: $O(N \cdot W + N \cdot K)$ which usually simplifies to $O(N \cdot W)$ since $W$ dominates $K$ in practice.
  - Per alignment, the inner loop runs $\sim N/W$ times.
  - Slicing `s[i - W : i]` takes $O(W)$ time.
  - Counter update and overcount check are $O(1)$.
  - The `while` loop for shrinking is bounded by $N/W$ total steps per alignment.
  - Comparing `curr == concated_words_freq` takes $O(K)$ time.
  - Total for one alignment: $(N/W) \cdot (W + K) = O(N + N \cdot K / W)$.
  - Across all $W$ alignments: $W \cdot O(N + N \cdot K / W) = O(N \cdot W + N \cdot K)$.
- **Space Complexity**: $O(N + K)$ space for storing the frequency Counter and the sliced sub-words.
