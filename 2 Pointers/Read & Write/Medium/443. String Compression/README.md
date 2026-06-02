# 443. String Compression

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/string-compression/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Two-pointer in-place string compression. We use a `read` pointer to iterate over groups of consecutive matching characters, and a `write` pointer to modify the array in-place.

## 2. How to Recognize the Pattern

- "Compress consecutive groups in-place" → two pointers to track group boundaries.
- "You must write your solution using only O(1) extra space" → in-place modification using a `write` pointer that trailing-follows the `read` pointer.
- Run-length encoding — count consecutive duplicates and overwrite existing indexes.

## 3. Why This Algorithm Fits

- The `read` pointer scans forward to find boundaries of repeating character blocks.
- The `write` pointer updates the original array at the correct positions. Because the compressed string length is always less than or equal to the uncompressed group length, the `write` pointer never overtakes the `read` pointer, avoiding corruption.
- No auxiliary string builders or arrays are used, resulting in true O(1) extra space.

## 4. How It Works

1. Initialize `write = 0` and `read = 0`.
2. While `read < len(chars)`:
   - Save the current character `char = chars[read]`.
   - Scan forward and increment `read` as long as `chars[read] == char` to measure `group_length`.
   - Write `char` to `chars[write]` and increment `write`.
   - If `group_length > 1`, convert `group_length` to string and write each digit to `chars[write]`, incrementing `write` for each digit.
3. Return `write` (the new length of the compressed array).

```python
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        
        while read < len(chars):
            char = chars[read]
            group_length = 0
            
            # Count the length of the current group
            while read < len(chars) and chars[read] == char:
                read += 1
                group_length += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if it's greater than 1
            if group_length > 1:
                for digit in str(group_length):
                    chars[write] = digit
                    write += 1
                    
        return write
```

### Dry Run Table
Input: `chars = ["a","a","b","b","c","c","c"]`

| group | char | read (initial) | read (after count) | group_length | Action Taken | chars State (modified portion) | write (after step) |
|-------|------|----------------|--------------------|--------------|--------------|--------------------------------|-------------------|
| *init*| -    | 0              | 0                  | -            | -            | `["a","a","b","b","c","c","c"]` | 0                 |
| 1     | 'a'  | 0              | 2                  | 2            | Write 'a', write '2' | `["a", "2", ...]` | 2                 |
| 2     | 'b'  | 2              | 4                  | 2            | Write 'b', write '2' | `["a", "2", "b", "2", ...]` | 4                 |
| 3     | 'c'  | 4              | 7                  | 3            | Write 'c', write '3' | `["a", "2", "b", "2", "c", "3", "c"]` | 6            |

**Final Result**: `write = 6`, compressed array prefix = `["a", "2", "b", "2", "c", "3"]`.

---

## 5. Time & Space Complexity

- **Time Complexity**: O(N) where N is the length of `chars`. Each character is visited at most twice (once by the `read` pointer and once when writing/converting).
- **Space Complexity**: O(1) auxiliary space as we modify the input array in-place without any extra space except for a few variables.
