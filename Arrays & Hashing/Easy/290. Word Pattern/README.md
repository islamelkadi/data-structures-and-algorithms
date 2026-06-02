# 290. Word Pattern

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/word-pattern/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Bidirectional word-to-pattern mapping using two hashmaps to enforce a strict one-to-one correspondence (bijection) between words and pattern characters.

## 2. How to Recognize the Pattern

- **Exact one-to-one correspondence**: "Each word must correspond to exactly one pattern character and vice versa" indicates a bijection check, which requires two hashmaps (or one map and a set to check unique values).
- **Same structure as Isomorphic Strings (205)**: The logic is identical, except we split the string `s` into a list of words instead of individual characters.
- **Length mismatch**: If the number of words does not equal the length of the pattern, it is an immediate `False`.

## 3. Why This Algorithm Fits

- The algorithm performs a single pass over the zipped word list and pattern, yielding $O(N)$ time.
- Two separate dictionaries detect mapping conflicts in both directions in $O(1)$ lookup time per element.

## 4. How It Works

1. Split the string `s` by spaces to get `s_list`.
2. If `len(s_list) != len(pattern)`, return `False`.
3. Initialize `char_to_word` (`word -> char`) and `word_to_char` (`char -> word`).
4. Iterate through the zipped pairs of `(word, char)`:
   - Check if the word is already mapped to a different character.
   - Check if the character is already mapped to a different word.
   - If either conflict occurs, return `False`.
   - Otherwise, update both maps.
5. If the loop finishes without any conflicts, return `True`.

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        # Edge case: number of words does not match number of chars
        if len(s_list) != len(pattern):
            return False

        # Look ups in two dicts
        char_to_word = {}
        word_to_char = {}
        for char, word in zip(s_list, pattern):
            if char in char_to_word and char_to_word[char] != word:
                    return False
            elif word in word_to_char and word_to_char[word] != char:
                    return False    
            char_to_word[char] = word
            word_to_char[word] = char
        return True
```

### Dry Run Table
Input: `pattern = "abba"`, `s = "dog cat cat dog"`  
`s_list = ["dog", "cat", "cat", "dog"]`

| char (word) | word (char) | char_to_word conflict? | word_to_char conflict? | action |
|-------------|-------------|------------------------|------------------------|--------|
| "dog"       | "a"         | no                     | no                     | `char_to_word["dog"] = "a"`, `word_to_char["a"] = "dog"` |
| "cat"       | "b"         | no                     | no                     | `char_to_word["cat"] = "b"`, `word_to_char["b"] = "cat"` |
| "cat"       | "b"         | `char_to_word["cat"] == "b"` (ok) | `word_to_char["b"] == "cat"` (ok) | ok |
| "dog"       | "a"         | `char_to_word["dog"] == "a"` (ok) | `word_to_char["a"] == "dog"` (ok) | ok |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N + M)$ where $N$ is the length of `s` (to split the string) and $M$ is the number of words/pattern length. Iterating through the elements takes $O(M)$ time.
- **Space Complexity**: $O(M + K)$ where $M$ is the number of words stored in `s_list` and $K$ is the number of unique words/characters stored in the maps.
