# 271. Encode and Decode Strings
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/encode-and-decode-strings/

## 1. Algorithm Used

Length-delimited serialization: each string is prefixed with its length and a `#` delimiter so the decoder can slice exactly the right number of characters without ambiguity.

## 2. How to Recognize the Pattern

- "serialize a list of strings into one string and recover it exactly" → need a self-describing format → length prefix.
- Simple delimiters (comma, space) fail when strings contain those characters → length prefix sidesteps the issue entirely.
- The decoder needs to know where each string ends without scanning for a terminator.

## 3. Why This Algorithm Fits

- O(n) time for both encode and decode — each character is written or read exactly once.
- O(n) space — the encoded string is proportional to the total character count.
- Length-prefix encoding is unambiguous regardless of the characters inside each string.

## 4. How It Works

**Encode:** for each string, prepend `str(len(string)) + "#"` then append the string itself. The `#` acts as a separator between the length digits and the string content.

**Decode:** walk the encoded string with an index. Accumulate digits until a `#` is found, parse the length, then slice exactly that many characters starting after the `#`. Advance the index past the sliced string and repeat.

```python
# Encode
encoded = ""
for s in strs:
    encoded += str(len(s)) + "#" + s

# Decode
result, i, length_str = [], 0, ""
while i < len(s):
    if s[i] != "#":
        length_str += s[i]
    else:
        result.append(s[i + 1: i + 1 + int(length_str)])
        i += int(length_str)
        length_str = ""
    i += 1
```

The key insight is that storing the length explicitly makes the `#` delimiter unambiguous — even if the string content contains `#` characters, the decoder always knows exactly how many bytes to consume.

Input: `strs = ["hello", "world"]`

Encode:
| string | encoded chunk |
|--------|---------------|
| "hello" | "5#hello" |
| "world" | "5#world" |
| result | "5#hello5#world" |

Decode `"5#hello5#world"`:
| i | char | length_str | action | result |
|---|------|------------|--------|--------|
| 0-0 | 5 | "5" | digit | |
| 1 | # | — | slice [2:7]="hello", i=7 | ["hello"] |
| 7-7 | 5 | "5" | digit | |
| 8 | # | — | slice [9:14]="world", i=14 | ["hello","world"] |
