## 1. Algorithm Used

Two-pointer inward traversal with hash set lookup.

## 2. How to Recognize the Pattern

- "Reverse only the vowels" → selective reversal → two pointers from both ends, swapping only when both point to vowels.
- Need O(1) vowel checks → hash set.
- String is immutable in Python → convert to list for in-place swaps.

## 3. Why This Algorithm Fits

- O(n) time — each pointer moves inward, total moves at most n.
- O(n) space — for the list copy (unavoidable since strings are immutable).
- The vowel set is fixed size (10 elements), so lookups are O(1).

## 4. How It Works

Convert string to a list. Place pointers at both ends. If left isn't a vowel, advance it. If right isn't a vowel, retreat it. If both are vowels, swap and move both inward. Join and return.

```python
vowels = set("aeiouAEIOU")
s = list(s)
left, right = 0, len(s) - 1
while left < right:
    if s[left] not in vowels:
        left += 1
    if s[right] not in vowels:
        right -= 1
    if s[left] in vowels and s[right] in vowels:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
return "".join(s)
```