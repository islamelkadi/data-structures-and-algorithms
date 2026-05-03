# 392. Is Subsequence

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/is-subsequence/

## 1. Algorithm Used

Same-direction two pointers: slow pointer advances through `s` only on a match, fast pointer iterates through every character of `t`.

## 2. How to Recognize the Pattern

- "Does s appear in t in order, with possible gaps?" → subsequence check → slow pointer on the pattern, fast pointer on the text.
- Characters must appear in the same relative order → scan both strings left to right, advance the pattern pointer only on a match.
- Early termination possible → if the pattern pointer reaches `len(s)`, the answer is immediately true.

## 3. Why This Algorithm Fits

- O(n) time — one pass through `t` (length n), at most one pass through `s` (length m).
- O(1) space — only a single integer pointer, no extra data structures.
- Order is preserved automatically because `slow_pointer` only advances forward, so it can never match an out-of-order character.

## 4. How It Works

`slow_pointer` tracks how many characters of `s` have been matched so far. For each character in `t`, if it equals `s[slow_pointer]`, increment `slow_pointer`. If `slow_pointer` reaches `len(s)`, all characters of `s` were found in order inside `t`, so return `True`. If the loop ends without that happening, return `False`.

```python
slow_pointer = 0
for char in t:
    if char == s[slow_pointer]:
        slow_pointer += 1
    if slow_pointer == len(s):
        return True
return False
```

The key insight is that order is enforced implicitly — `slow_pointer` never moves backward, so a match at position `i` in `t` can only be used for the current character of `s`, not a later one.
