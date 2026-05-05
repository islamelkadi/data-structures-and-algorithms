# 217. Contains Duplicate
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/contains-duplicate/

## 1. Algorithm Used

Hash set membership check with early exit on the first repeated element.

## 2. How to Recognize the Pattern

- "return true if any value appears more than once" → track seen values → hash set.
- No need to count occurrences — presence alone is sufficient → set over Counter.
- Early exit is possible the moment a duplicate is found.

## 3. Why This Algorithm Fits

- O(n) time — each element is inserted and looked up in O(1) amortized.
- O(n) space — the set holds at most n elements in the worst case (all unique).
- A set is simpler and faster than sorting (O(n log n)) for this problem.

## 4. How It Works

Iterate through the array. Before adding each number to the set, check whether it is already present. If it is, a duplicate exists and True is returned immediately. If the loop completes without a hit, all elements are unique and False is returned.

```python
hashset = set()
for num in nums:
    if num in hashset:
        return True
    hashset.add(num)
return False
```

The single-pass approach means the function exits as soon as the first duplicate is found rather than scanning the entire array.

Input: `nums = [1, 2, 3, 1]`

| num | in hashset? | action | hashset |
|-----|-------------|--------|---------|
| 1 | no | add | {1} |
| 2 | no | add | {1,2} |
| 3 | no | add | {1,2,3} |
| 1 | yes | return True | |
