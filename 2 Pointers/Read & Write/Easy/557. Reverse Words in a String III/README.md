# 557. Reverse Words in a String III

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/reverse-words-in-a-string-iii/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

## 1. Algorithm Used

Split on spaces, then apply opposite-direction two pointers to reverse each word's characters in-place, then rejoin.

## 2. How to Recognize the Pattern

- "Reverse each word individually, keep word order" → per-word reversal → split, reverse each, join.
- Each word reversal is the same symmetric swap problem as 344 → left/right pointers converging inward.
- Words are separated by single spaces → `split(" ")` gives clean word boundaries.

## 3. Why This Algorithm Fits

- O(n) time — splitting is O(n), reversing all characters across all words is O(n) total, joining is O(n).
- O(n) space — the character list for each word and the result list.
- Delegating the reversal to a helper keeps the logic for each word identical to a standalone reverse-string problem.

## 4. How It Works

Split the sentence on spaces to get individual words. For each word, convert it to a character list and use `left`/`right` pointers to swap characters from both ends inward until they meet. Rejoin the reversed characters into a string and collect results. Finally, join all reversed words with a single space.

```python
def reverseWord(word):
    chars = list(word)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

words = s.split(" ")
return ' '.join(reverseWord(w) for w in words)
```

The word order in the sentence is never touched — only the characters within each word are reversed.

Input: `s = "Let's take LeetCode contest"`

| word | reverseWord result |
|------|--------------------|
| "Let's" | "s'teL" |
| "take" | "ekat" |
| "LeetCode" | "edoCteeL" |
| "contest" | "tsetnoC" |
| joined | "s'teL ekat edoCteeL tsetnoC" |
