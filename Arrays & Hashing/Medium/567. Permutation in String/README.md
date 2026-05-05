# 567. Permutation in String
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/permutation-in-string/

## 1. Algorithm Used

Fixed-size sliding window with frequency map comparison: maintain a Counter of the current window in s2 and slide it one character at a time, comparing against the Counter of s1.

## 2. How to Recognize the Pattern

- "does s2 contain a permutation of s1" → any permutation has the same character frequencies → frequency map equality.
- The window size is fixed at `len(s1)` → fixed-size sliding window.
- Slide by adding the incoming character and removing the outgoing character rather than rebuilding the Counter each step.

## 3. Why This Algorithm Fits

- O(n) time — each character in s2 is added and removed from the window Counter exactly once.
- O(k) space — both Counters hold at most k distinct characters (k ≤ 26 for lowercase letters).
- Incrementally updating the window Counter is O(1) per step versus O(len(s1)) to rebuild it from scratch.

## 4. How It Works

Initialize the window Counter with the first `len(s1)` characters of s2 and check for an immediate match. Then slide the window forward: for each new position, add the incoming head character and decrement (and delete if zero) the outgoing tail character. After each slide, compare the window Counter to the s1 Counter.

```python
window_size = len(s1)
s1_hashmap = Counter(s1)
s2_hashmap = Counter(s2[:window_size])

if s1_hashmap == s2_hashmap:
    return True

for i in range(window_size, len(s2)):
    head = s2[i]
    s2_hashmap[head] = s2_hashmap.get(head, 0) + 1

    tail = s2[i - window_size]
    s2_hashmap[tail] -= 1
    if s2_hashmap[tail] == 0:
        del s2_hashmap[tail]

    if s1_hashmap == s2_hashmap:
        return True

return False
```

Deleting a key when its count reaches zero is important: it keeps the window Counter clean so that Counter equality checks work correctly without spurious zero-count entries causing false mismatches.

Input: `s1 = "ab"`, `s2 = "eidbaooo"`

| i | head | tail | s2_hashmap | == s1_hashmap? |
|---|------|------|------------|----------------|
| init | — | — | {e:1,i:1} | {a:1,b:1}? no |
| 2 | d | e | {i:1,d:1} | no |
| 3 | b | i | {d:1,b:1} | no |
| 4 | a | d | {b:1,a:1} | yes → return True |
