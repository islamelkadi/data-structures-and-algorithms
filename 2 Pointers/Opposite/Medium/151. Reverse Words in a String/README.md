# 151. Reverse Words in a String

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/reverse-words-in-a-string/

## 1. Algorithm Used

Split (handles multiple spaces automatically), then opposite-direction two pointers to reverse the word list, then rejoin with a single space.

## 2. How to Recognize the Pattern

- "Reverse the order of words, trim extra spaces" → split on whitespace, reverse the word list → two pointers on the word array.
- Leading/trailing spaces and multiple spaces between words → `str.split()` (no argument) collapses all whitespace and strips edges in one call.
- Reversing a list in-place → same left/right swap pattern as reversing a character array.

## 3. Why This Algorithm Fits

- O(n) time — splitting is O(n), the two-pointer reversal is O(w) where w is the number of words, joining is O(n).
- O(n) space — the list of words.
- `split()` without arguments is the idiomatic Python way to handle variable whitespace; it avoids any manual trimming or filtering.

## 4. How It Works

Call `s.split()` to tokenize on any whitespace, producing a clean list of words with no empty strings. Place `left` at 0 and `right` at the last index. Swap words at both pointers and converge inward until they meet. Join the reversed list with a single space.

```python
s = s.split()
left, right = 0, len(s) - 1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
return " ".join(s)
```

The difference from problem 557 is that here the word order is reversed (not the characters within each word), and `split()` without an argument handles messy whitespace for free.

Input: `s = "  the sky  is blue  "`

| step | action | state |
|------|--------|-------|
| split | `s.split()` | `["the", "sky", "is", "blue"]` |
| left=0, right=3 | swap "the" ↔ "blue" | `["blue", "sky", "is", "the"]` |
| left=1, right=2 | swap "sky" ↔ "is" | `["blue", "is", "sky", "the"]` |
| left=2, right=1 | left >= right → stop | |
| join | `" ".join(...)` | `"blue is sky the"` |
