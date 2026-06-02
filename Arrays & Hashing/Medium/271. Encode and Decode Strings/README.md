# 271. Encode and Decode Strings

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/encode-and-decode-strings/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Length-delimited serialization: each string is prefixed with its length and a `#` delimiter so the decoder can slice exactly the right number of characters without ambiguity.

## 2. How to Recognize the Pattern

- **Serialize and deserialize a list of strings**: Converting a collection of strings into a single string for transmission and then recovering it requires a custom serialization format.
- **Handling arbitrary characters**: Simple delimiters (like commas or spaces) fail if the strings themselves contain those characters. Prefixing each chunk with its length sidesteps this issue entirely.
- **Ambiguity resolution**: The decoder reads the length prefix to know exactly how many characters to slice, preventing parsing issues.

## 3. Why This Algorithm Fits

- Both encoding and decoding process each character in $O(1)$ time, yielding $O(N)$ total time complexity.
- Storing the length explicitly makes the `#` delimiter unambiguous: even if the string content contains `#`, the decoder skips over them because it knows exactly how many characters to consume based on the prefix.

## 4. How It Works

- **Encode**: For each string, prepend `str(len(string)) + "#"` followed by the string itself. The `#` separates the length digits from the actual content.
- **Decode**: Walk through the encoded string with a pointer `current_index`:
  - Accumulate characters in `string_len` until reaching `#`.
  - Once `#` is found, parse `string_len` to get the string's length.
  - Slice the next `int(string_len)` characters from the encoded string.
  - Append the sliced string to our results list.
  - Move `current_index` forward by the length of the string and reset `string_len`.

```python
class Codec:
    def __init__(self):
        self.delim = "#"

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""

        encoded_string = ""
        for str_ in strs:
            encoded_string += str(len(str_)) + self.delim + str_
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []

        decoded_string_list = []
        current_index = 0
        string_len = ""
        while current_index < len(s):
            if s[current_index] != self.delim:
                string_len += s[current_index]
            else:
                decoded_string_list.append(s[current_index + 1: current_index + 1 + int(string_len)])
                current_index += int(string_len)
                string_len = ""
            current_index += 1
        return decoded_string_list
```

### Dry Run Table
Input: `strs = ["hello", "world"]`

#### Encoding
| string | encoded chunk |
|--------|---------------|
| "hello" | "5#hello" |
| "world" | "5#world" |
| **Result** | `"5#hello5#world"` |

#### Decoding `"5#hello5#world"`
| current_index | s[current_index] | string_len | action | decoded_string_list |
|---|---|---|---|---|
| 0 | "5" | "5" | digit | `[]` |
| 1 | "#" | — | slice `[2:7]` = `"hello"`, advance `current_index` by 5 | `["hello"]` |
| 7 | "5" | "5" | digit | `["hello"]` |
| 8 | "#" | — | slice `[9:14]` = `"world"`, advance `current_index` by 5 | `["hello", "world"]` |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ for both `encode` and `decode`, where $N$ is the total number of characters across all strings.
- **Space Complexity**: $O(N)$ to store the serialized string and the final decoded output.
