# 1832. Check if the Sentence Is Pangram

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm utilizes a Hash Set to collect all unique characters present in the input sentence. It then compares the size of this set to the size of the English alphabet (26) to determine if all letters have appeared.

## 2. How to Recognize the Pattern

- **Pangram Check / Unique Element Counting**: The definition of a pangram is a sentence containing every letter of the alphabet at least once. Since duplicate letters do not matter, we only care about the *unique* characters present. A Hash Set is the standard tool to filter out duplicates in linear time.
- **Fixed-Alphabet Optimization**: The English alphabet has a fixed size of 26. This allows us to perform a constant-space comparison.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ where $N$ is the length of `sentence`. We traverse the sentence once to construct the set of characters.
- **Space Complexity**: $O(1)$ auxiliary space. Although we build a set, it contains at most 26 unique English characters regardless of how large the input `sentence` is.

## 4. How It Works

1. Create a set `alphabet` containing all 26 lowercase English letters and store its length (`alphabet_len = 26`).
2. Construct a set `dic` from `sentence` via set comprehension.
3. Return `True` if `len(dic) == alphabet_len`, indicating all 26 alphabet characters are present, and `False` otherwise.

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        alphabet_len = len(alphabet)
        
        dic = {letter for letter in sentence}
        return alphabet_len == len(dic)
```

### Dry Run Table
Input: `sentence = "thequickbrownfoxjumpsoverthelazydog"`

| Step/Index | Character | `dic` Size | Condition (`len(dic) == 26`) | Action Taken |
|------------|-----------|------------|-----------------------------|--------------|
| *init*     | —         | 0          | —                           | Initialize `alphabet` and set `alphabet_len = 26` |
| 1          | 't'       | 1          | —                           | Add `'t'` to `dic` |
| 2          | 'h'       | 2          | —                           | Add `'h'` to `dic` |
| ...        | ...       | ...        | —                           | Add remaining characters to `dic` |
| End of loop| —         | 26         | `26 == 26` (True)           | Return `True` |
