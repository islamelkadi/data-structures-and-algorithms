# 58. Length of Last Word

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/length-of-last-word/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Reverse iteration with flag-based word boundary detection.

## 2. How to Recognize the Pattern

- **Find length of the last word**: Scanning from the back of the string ($N-1$ down to $0$) allows us to ignore the rest of the string, which is highly efficient.
- **Messy trailing spaces**: Trailing spaces must be ignored. We only start counting letters after encountering the first non-space character, and stop when we see the next space character.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: In the worst case, we traverse the entire string once. For most cases, we exit early after processing only the last word.
- **$O(1)$ space**: Unlike `s.split()`, which allocates list memory proportional to the number of words, this approach uses a constant amount of memory.

## 4. How It Works

We traverse the string from the last index (`len(s) - 1`) backwards:
1. When we encounter a non-space character, we set `letter_encountered_yet = True`.
2. While `letter_encountered_yet` is True, we increment `letters_encountered` for each alphabetical character we see.
3. Once we encounter a space while `letter_encountered_yet` is True, we have reached the beginning boundary of the last word, so we break the loop.

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_encountered_yet = False
        letters_encountered = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                letter_encountered_yet = True
            
            if letter_encountered_yet and s[i].isalpha():
                letters_encountered += 1
            
            if s[i] == " " and letter_encountered_yet:
                break
        return letters_encountered
```

### Dry Run Table
Input: `s = "Hello World "`

| i | s[i] | s[i] != " "? | letter_encountered_yet | s[i].isalpha()? | letters_encountered | Action |
|---|---|---|---|---|---|---|
| 11 | `" "` | no | False | no | 0 | *Skip trailing space* |
| 10 | `"d"` | yes | True | yes | 1 | Increment count |
| 9 | `"l"` | yes | True | yes | 2 | Increment count |
| 8 | `"r"` | yes | True | yes | 3 | Increment count |
| 7 | `"o"` | yes | True | yes | 4 | Increment count |
| 6 | `"W"` | yes | True | yes | 5 | Increment count |
| 5 | `" "` | no | True | no | 5 | Space after word start $\to$ `break` |

Result: `5`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of `s`. We scan at most $N$ characters.
- **Space Complexity**: $O(1)$ auxiliary space since we only store two boolean/integer trackers.
