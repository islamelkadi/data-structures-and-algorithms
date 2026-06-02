# 1456. Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium
**Link:** [LeetCode URL](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm utilizes a Fixed-Size Sliding Window of length `k`. It maintains a running count of vowels inside the window, adjusting the count in $O(1)$ time by inspecting only the character entering and the character leaving the window at each slide step. Vowel membership is optimized to $O(1)$ using a Hash Set.

## 2. How to Recognize the Pattern

- **Substring of Given Length**: The problem asks to find a maximum value over all substrings of a *fixed length* `k`. This is a classic indicator of a fixed-size sliding window.
- **Incremental State Updating**: Rather than re-evaluating each window from scratch—which would cost $O(N \cdot K)$—we can adjust our vowel count in $O(1)$ time per slide by adding the incoming character and subtracting the outgoing character.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ — We make a single pass to count vowels in the initial window of size $k$ ($O(k)$) and another pass to slide the window to the end of the string ($O(N - k)$).
- **Space Complexity**: $O(1)$ — The lookup set is bounded to exactly 5 elements (`{'a', 'e', 'i', 'o', 'u'}`), requiring constant auxiliary space.

## 4. How It Works

1. Initialize a hash set containing all five English vowels for $O(1)$ membership checks.
2. Calculate the vowel count `curr` in the first window `s[0...k-1]`. Initialize the answer `ans = curr`.
3. Slide the window from left to right by looping index `i` from `k` to `len(s) - 1`:
   - If the element leaving the window at index `i - k` is a vowel, decrement `curr`.
   - If the element entering the window at index `i` is a vowel, increment `curr`.
   - Update `ans` with the maximum value: `ans = max(ans, curr)`.
4. Return `ans`.

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        ans = curr
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                curr -= 1
            if s[i] in vowels:
                curr += 1
            ans = max(curr, ans)
        return ans
```

### Dry Run Table
Input: `s = "abciiidef"`, `k = 3`

| Step/Index (`i`) | Incoming char `s[i]` | Outgoing char `s[i - k]` | `curr` | `ans` | Action Taken |
|------------------|----------------------|--------------------------|--------|-------|--------------|
| *init*           | —                    | —                        | 1      | 1     | Process first window `s[0...2]` (`"abc"` has `'a'`) |
| 3                | `'i'` (vowel)        | `'a'` (vowel)            | 1      | 1     | `curr += 1 - 1 = 1` |
| 4                | `'i'` (vowel)        | `'b'` (non-vowel)        | 2      | 2     | `curr += 1 - 0 = 2`, update `ans` |
| 5                | `'i'` (vowel)        | `'c'` (non-vowel)        | 3      | 3     | `curr += 1 - 0 = 3`, update `ans` |
| 6                | `'d'` (non-vowel)    | `'i'` (vowel)            | 2      | 3     | `curr += 0 - 1 = 2` |
| 7                | `'e'` (vowel)        | `'i'` (vowel)            | 2      | 3     | `curr += 1 - 1 = 2` |
| 8                | `'f'` (non-vowel)    | `'i'` (vowel)            | 1      | 3     | `curr += 0 - 1 = 1` |
