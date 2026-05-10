## 1. Algorithm Used

Row simulation with a direction flag — distribute characters into row buckets by bouncing a row tracker up and down, then concatenate.

## 2. How to Recognize the Pattern

- "Rearrange characters in a zigzag pattern" → simulate the traversal → assign each character to its row bucket.
- The row index oscillates between 0 and numRows-1, reversing direction at each boundary.
- Output is rows read left to right → just join the buckets in order.

## 3. Why This Algorithm Fits

- O(n) time — single pass through the string.
- O(n) space — the row buckets collectively hold all n characters.
- Simulating the zigzag directly is simpler than computing index math for each character.

## 4. How It Works

Maintain `r_tracker` (current row) and `is_down` (direction). For each character, append it to `zig_zag[r_tracker]`, then move the tracker. When the tracker hits row 0 or row numRows-1, flip the direction. The `numRows == 1` guard avoids an infinite direction flip at the only boundary.

```python
if numRows == 1:
    return s

r_tracker, is_down = 0, True
zig_zag = ["" for _ in range(numRows)]

for char_ in s:
    zig_zag[r_tracker] += char_
    r_tracker += 1 if is_down else -1
    if r_tracker in (0, numRows - 1):
        is_down = not is_down

return "".join(zig_zag)
```

Input: `s = "PAYPALISHIRING"`, `numRows = 3`

| char | r_tracker | is_down | zig_zag |
|------|-----------|---------|---------|
| P | 0 | True→flip | ["P","",""] |
| A | 1 | True | ["P","A",""] |
| Y | 2 | True→flip | ["P","A","Y"] |
| P | 1 | False | ["P","AP","Y"] |
| A | 0 | False→flip | ["PA","AP","Y"] |
| L | 1 | True | ["PA","APL","Y"] |
| I | 2 | True→flip | ["PA","APL","YI"] |
| S | 1 | False | ["PA","APLS","YI"] |
| H | 0 | False→flip | ["PAH","APLS","YI"] |
| I | 1 | True | ["PAH","APLSI","YI"] |
| R | 2 | True→flip | ["PAH","APLSI","YIR"] |
| I | 1 | False | ["PAH","APLSII","YIR"] |
| N | 0 | False→flip | ["PAHN","APLSII","YIR"] |
| G | 1 | True | ["PAHN","APLSIIG","YIR"] |
| result | | | "PAHNAPLSIIGYIR" |

## 5. Time & Space Complexity

Time: O(n) — single pass through the string.

Space: O(n) — row buckets store all characters.
