## 1. Algorithm Used

Variable-size sliding window with hash set for duplicate detection.

## 2. How to Recognize the Pattern

- "Longest substring without repeating characters" → longest contiguous window with a uniqueness constraint.
- "No repeats" in a window → set to track what's currently in the window.
- Window expands right freely, shrinks left when a duplicate is found → variable sliding window.

## 3. Why This Algorithm Fits

- The set gives O(1) lookups to check if a character is already in the window.
- Shrinking from the left removes characters until the duplicate is gone — this maintains the invariant that the window has all unique characters.
- Both options work. The hash set (Option 2) is cleaner because you only care about presence, not counts. The hash map (Option 1) is useful if you needed to track frequencies for a different constraint.

## 4. How It Works

Expand the window by adding `s[i]`. If `s[i]` is already in the set, shrink from the left — remove `s[left]` from the set and advance `left` — until the duplicate is gone. Then add `s[i]` and update the max length.

```python
left = ans = 0
seen = set()
for i in range(len(s)):
    while s[i] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[i])
    ans = max(ans, i - left + 1)
return ans
```

Example with `s = "abcabcbb"`:
- `a,b,c` → window grows, seen={a,b,c}, ans=3
- `a` again → shrink: remove `a`, left=1. seen={b,c}. Add `a`, seen={b,c,a}, ans=3
- `b` again → shrink: remove `b`, left=2. seen={c,a}. Add `b`, seen={c,a,b}, ans=3
- And so on. Max stays 3.

Input: `s = "abcabcbb"`

| i | s[i] | in seen? | shrink | left | seen | ans |
|---|------|----------|--------|------|------|-----|
| 0 | a | no | — | 0 | {a} | 1 |
| 1 | b | no | — | 0 | {a,b} | 2 |
| 2 | c | no | — | 0 | {a,b,c} | 3 |
| 3 | a | yes | remove a, left=1 | 1 | {b,c,a} | 3 |
| 4 | b | yes | remove b, left=2 | 2 | {c,a,b} | 3 |
| 5 | c | yes | remove c, left=3 | 3 | {a,b,c} | 3 |
| 6 | b | yes | remove a, remove b, left=5 | 5 | {c,b} | 3 |
| 7 | b | yes | remove c, remove b, left=7 | 7 | {b} | 3 |

## 5. Time & Space Complexity

Time: O(n) — each character is added to the set once and removed at most once. Both `i` and `left` move forward only, so total operations across all iterations is at most 2n.

Space: O(min(n, m)) where m is the character set size (e.g., 26 for lowercase, 128 for ASCII). The set holds at most one of each unique character in the current window.