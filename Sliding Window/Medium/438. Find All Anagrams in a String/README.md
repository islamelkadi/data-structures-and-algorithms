## 1. Algorithm Used

Sliding window with two frequency hashmaps.

## 2. How to Recognize the Pattern

- "Find all substrings that are anagrams of p" → fixed-concept window (same character set as p).
- Anagram = same characters, same counts → hashmap comparison.
- Shrink from the left whenever a character is invalid or over-counted.

## 3. Why This Algorithm Fits

- O(n) time — each character is added once and removed at most once.
- Shrinking only when a character is over-counted keeps the window as large as possible.
- Comparing two hashmaps is O(1) since the alphabet is fixed size (26 letters).

## 4. How It Works

Maintain `p_hashmap` (fixed) and `s_hashmap` (sliding window). Expand `right` each iteration. If `s[right]` is over-counted relative to `p_hashmap`, shrink from `left` until it's valid. When both maps are equal, the window is an anagram — record `left`.

```python
for right in range(len(s)):
    s_hashmap[s[right]] += 1

    while s_hashmap[s[right]] > p_hashmap.get(s[right], 0):
        shrink_left()
        left += 1

    if s_hashmap == p_hashmap:
        indices.append(left)
```

Example with `s = "cbaebabacd"`, `p = "abc"`:
- right=2: window "cba" == p_hashmap → append 0
- right=6: window "bac" == p_hashmap → append 6
- Result: `[0, 6]`

Input: `s = "cbaebabacd"`, `p = "abc"`, `p_hashmap = {a:1,b:1,c:1}`

| right | s[right] | s_hashmap | shrink? | == p_hashmap? | indices |
|-------|---------|-----------|---------|---------------|---------|
| 0 | c | {c:1} | no | no | [] |
| 1 | b | {c:1,b:1} | no | no | [] |
| 2 | a | {c:1,b:1,a:1} | no | yes | [0] |
| 3 | e | {c:1,b:1,a:1,e:1} | e>0 → shrink c,b,a,left=3 | no | [0] |
| 4 | b | {e:1,b:1} | no | no | [0] |
| 5 | a | {e:1,b:1,a:1} | no | no | [0] |
| 6 | b | {e:1,b:2,a:1} | b>1 → shrink e,left=4 | {b:2,a:1}≠p | [0] |
| 6 | b | {b:2,a:1} | b>1 → shrink b,left=5 | {b:1,a:1}≠p | [0] |
| 6 | b | {b:1,a:1} | no | no | [0] |
| 7 | a | {b:1,a:2} | a>1 → shrink b,left=6 | {a:2}≠p | [0] |
| 7 | a | {a:2} | a>1 → shrink a,left=7 | {a:1}≠p | [0] |
| 8 | c | {a:1,c:1} | no | no | [0] |
| 9 | d | {a:1,c:1,d:1} | d>0 → shrink a,left=8 | no | [0] |
| 9 | d | {c:1,d:1} | d>0 → shrink c,left=9 | no | [0] |
| 9 | d | {d:1} | d>0 → shrink d,left=10 | {} ≠ p | [0] |

## 5. Time & Space Complexity

Time: O(n) — each character enters and leaves the window at most once.

Space: O(1) — hashmaps are bounded by alphabet size (26).
