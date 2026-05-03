## 1. Algorithm Used

Two-pointer inward comparison on a cleaned string.

## 2. How to Recognize the Pattern

- "Is it the same forwards and backwards?" → palindrome check → compare from both ends toward the middle.
- The string has non-alphanumeric characters and mixed case → clean it first, then compare.
- Two pointers moving inward is the classic O(n) palindrome approach.

## 3. Why This Algorithm Fits

- O(n) time — one pass to clean, one pass to compare.
- O(n) space — for the cleaned string. (Could be O(1) space by skipping non-alnum chars in-place with the pointers, but this is cleaner to read.)
- Early return on first mismatch avoids unnecessary comparisons.

## 4. How It Works

Strip out everything that isn't a letter or digit and lowercase the result. Then place one pointer at the start and one at the end. Compare characters at both pointers — if they ever differ, it's not a palindrome. Move inward each step. If the pointers meet without a mismatch, it's a palindrome.

```python
s = "".join(x.lower() for x in s if x.isalnum())
left, right = 0, len(s) - 1
while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1
return True
```

Cleaning first keeps the pointer logic dead simple — no need to skip special characters during comparison.