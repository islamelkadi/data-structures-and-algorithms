## 1. Algorithm Used

Two-pointer group detection with flush-on-change.

## 2. How to Recognize the Pattern

- "Compress consecutive groups in-place" → two pointers to track group boundaries.
- `left` marks the start of a group, `right` scans forward until the character changes.
- Run-length encoding — count consecutive duplicates and write `char + count`.

## 3. Why This Algorithm Fits

- Two pointers naturally track group start and end without extra data structures.
- The lambda extracts the repeated flush logic — write the character, and the count only if > 1.
- Writing back into `chars` at the end satisfies the in-place requirement.

## 4. How It Works

`left` stays at the start of the current group. `right` scans forward. When `chars[right]` differs from `chars[left]`, flush the group (character + length if > 1) and move `left` to `right`. At the end of the array, flush the final group. Then overwrite `chars` with the compressed result.

```python
left = 0
compressed_string = ""
flush = lambda char, length: char + (str(length) if length > 1 else "")

for right in range(len(chars)):
    if chars[right] != chars[left]:
        compressed_string += flush(chars[left], right - left)
        left = right
    if right == len(chars) - 1:
        compressed_string += flush(chars[left], right - left + 1)

for i, char in enumerate(compressed_string):
    chars[i] = char
return len(compressed_string)
```

Example with `chars = ["a","a","b","b","c","c","c"]`:
- right=0,1: same as left(a), skip
- right=2: `b != a` → flush `"a2"`, left=2
- right=3: same as left(b), skip
- right=4: `c != b` → flush `"b2"`, left=4
- right=6: end of array → flush `"c3"`
- compressed_string = `"a2b2c3"`
- Write back into chars, return 6

Input: `chars = ["a","a","b","b","c","c","c"]`

| right | chars[right] | chars[left] | match? | compressed_string | left |
|-------|-------------|-------------|--------|-------------------|------|
| 0 | a | a | yes | "" | 0 |
| 1 | a | a | yes | "" | 0 |
| 2 | b | a | no → flush "a2" | "a2" | 2 |
| 3 | b | b | yes | "a2" | 2 |
| 4 | c | b | no → flush "b2" | "a2b2" | 4 |
| 5 | c | c | yes | "a2b2" | 4 |
| 6 | c | c | yes + end → flush "c3" | "a2b2c3" | 4 |

## 5. Time & Space Complexity

Time: O(n) — single pass through chars, plus O(n) to write back. Each element visited at most twice.

Space: O(n) — for `compressed_string`. Could be O(1) by writing directly into `chars` with a write pointer instead of building a separate string, but this approach is more readable.