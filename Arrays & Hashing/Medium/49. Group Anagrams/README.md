# 49. Group Anagrams

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/group-anagrams/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)
6. [6. Trade-offs](#6-trade-offs)

## 1. Algorithm Used

Hash Map grouping with character frequency array mapping (optionally sorting-based grouping).

## 2. How to Recognize the Pattern

- **Group anagrams**: Words containing identical characters with identical frequencies require a canonical/normalised key representing that group.
- **Bucketing by key**: A hash map (`defaultdict(list)`) is used to map derived keys to lists of strings.

## 3. Why This Algorithm Fits

- Single-pass over the word list.
- Using a 26-element character count tuple as the key runs in $O(K)$ time per word of length $K$, giving $O(N \cdot K)$ overall time complexity.

## 4. How It Works

For each word, we count character frequencies to construct a 26-element tuple (representing counts of 'a' through 'z'). This tuple is unique to each anagram group and acts as the hash map key.

```python
from collections import defaultdict, Counter, OrderedDict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # Notice the requirements: string only consists of english letters
        #     # This maybe a clue to use 26 fixed chars
        # alphabets = "abcdefghijklmnopqrstuvwxyz"
        # alphabets_indexed = {key: index for index, key in enumerate(alphabets)}

        # grouped_anagrams = defaultdict(list)
        # for str_ in strs:
        #     alphabets_array = [0] * 26
        #     counted_str = Counter(str_)
        #     for alphabet, frequency in counted_str.items():
        #         alphabets_array[alphabets_indexed[alphabet]] = frequency
        #     grouped_anagrams[tuple(alphabets_array)].append(str_)
        
        # return list(grouped_anagrams.values())
        grouped_anagrams = defaultdict(list)
        for str_ in strs:
            alphabets_array = [0] * 26
            for alphabet in str_:
                alphabets_array[ord(alphabet) - ord("a")] += 1
            grouped_anagrams[tuple(alphabets_array)].append(str_)
        return list(grouped_anagrams.values())
```

Optionally, sorting the string (e.g. `"".join(sorted(word))`) can also serve as the hash map key:
```python
ordered_word = "".join(sorted(word))
anagram_hashmap[ordered_word].append(word)
```

### Dry Run Table
Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

| word | character frequency key | group after insert |
|---|---|---|
| `"eat"` | `(1, 0, ..., 1, ..., 1, ...)` (a=1, e=1, t=1) | `{"(eat-key)": ["eat"]}` |
| `"tea"` | `(1, 0, ..., 1, ..., 1, ...)` (a=1, e=1, t=1) | `{"(eat-key)": ["eat", "tea"]}` |
| `"tan"` | `(1, 0, ..., 1, ..., 1, ...)` (a=1, n=1, t=1) | `{"(eat-key)": [...], "(tan-key)": ["tan"]}` |
| `"ate"` | `(1, 0, ..., 1, ..., 1, ...)` (a=1, e=1, t=1) | `{"(eat-key)": ["eat", "tea", "ate"], ...}` |
| `"nat"` | `(1, 0, ..., 1, ..., 1, ...)` (a=1, n=1, t=1) | `{"(tan-key)": ["tan", "nat"], ...}` |
| `"bat"` | `(1, 1, ..., 0, ..., 1, ...)` (a=1, b=1, t=1) | `{"(bat-key)": ["bat"], ...}` |

Result: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

---

## 5. Time & Space Complexity

- **Time Complexity**:
  - **Character Count (Option 2)**: $O(N \cdot K)$ where $N$ is the number of strings and $K$ is the maximum length of a string. Iterating through each character takes $O(K)$ per word.
  - **Sorting (Option 1)**: $O(N \cdot K \log K)$ because sorting each string of length $K$ takes $O(K \log K)$ time.
- **Space Complexity**: $O(N \cdot K)$ auxiliary space to store the grouped anagrams in the hash map.

---

## 6. Trade-offs

### Option 1 (Sorting)
- **Pros**: Simpler and more readable. Plain string keys are lightweight to hash and allocate in memory.
- **Cons**: $O(K \log K)$ per word, which is slower for extremely long words.

### Option 2 (Frequency Array)
- **Pros**: $O(K)$ per word, offering optimal asymptotic time complexity.
- **Cons**: Allocating a 26-element list per word, converting it to a tuple, and hashing a large 26-element tuple introduces constant overhead that often runs slower than string sorting for short words in Python.
