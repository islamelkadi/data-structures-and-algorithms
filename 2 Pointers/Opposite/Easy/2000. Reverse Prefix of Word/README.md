# 2000. Reverse Prefix of Word

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/reverse-prefix-of-word/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm utilizes a Converging Two-Pointer (Opposite) approach. Once the first occurrence of the character `ch` is found, the prefix substring up to that index is converted into a list of characters and reversed in-place by swapping elements from both ends moving inwards.

## 2. How to Recognize the Pattern

- **In-place Reversal**: Any problem asking to reverse a sequence, string, or subset thereof is a primary candidate for converging two pointers.
- **Opposite Pointers**: One pointer starts at the beginning (`left = 0`) and the other starts at the end of the sequence to be reversed (`right = index(ch)`), and they converge until they meet or cross.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ where $N$ is the length of `word`. Finding the index of `ch` takes $O(N)$ time. Reversing the prefix of length $K$ (where $K \le N$) takes $O(K)$ swaps. Constructing the final string takes $O(N)$ time.
- **Space Complexity**: $O(N)$ space to create the mutable character list representation of the prefix and build the resulting string.

## 4. How It Works

1. Search for `ch` in `word`. If it does not exist, return `word` immediately.
2. Find the index of the first occurrence of `ch`, which acts as the right bound of our prefix (`final = word.index(ch)`).
3. Create a list of characters of the prefix: `sub_word = list(word[:final + 1])`.
4. Initialize `left = 0` and `right = final`.
5. Loop while `left < right`:
   - Swap `sub_word[left]` and `sub_word[right]`.
   - Increment `left` by 1.
   - Decrement `right` by 1.
6. Join the reversed prefix and concatenate it with the rest of the original string: `"".join(sub_word) + word[final + 1:]`.

```python
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        left = 0
        right = final = word.index(ch)
        sub_word = list(word[:right+1])
        while left < right:
            sub_word[left], sub_word[right] = sub_word[right], sub_word[left]
            left += 1
            right -= 1
        return "".join(sub_word) + word[final+1:]
```

### Dry Run Table
Input: `word = "abcdefd"`, `ch = "d"`  
`final = 3` (index of first `'d'`)  
`sub_word = ['a', 'b', 'c', 'd']`

| Step/Index | `left` | `right` | Condition (`left < right`) | `sub_word` | Action Taken |
|------------|--------|---------|---------------------------|------------|--------------|
| *init*     | 0      | 3       | —                         | `['a', 'b', 'c', 'd']` | Initialize pointers and prefix list |
| 1          | 0      | 3       | `0 < 3` (True)            | `['d', 'b', 'c', 'a']` | Swap indices 0 & 3; `left` $\to$ 1, `right` $\to$ 2 |
| 2          | 1      | 2       | `1 < 2` (True)            | `['d', 'c', 'b', 'a']` | Swap indices 1 & 2; `left` $\to$ 2, `right` $\to$ 1 |
| 3          | 2      | 1       | `2 < 1` (False)           | `['d', 'c', 'b', 'a']` | Terminate loop |
