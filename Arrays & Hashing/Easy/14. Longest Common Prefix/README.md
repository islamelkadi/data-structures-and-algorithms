# 14. Longest Common Prefix
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/longest-common-prefix/

## 1. Algorithm Used

Vertical scanning with set-size check across all strings column by column.

## 2. How to Recognize the Pattern

- "find the prefix shared by all strings" → scan character positions left to right → stop at the first mismatch.
- The prefix can be no longer than the shortest string → find the minimum length first.
- Checking all strings at a single column position is equivalent to asking whether a set of those characters has size 1.

## 3. Why This Algorithm Fits

- O(S) time — S is the total number of characters across all strings; in the worst case every character is visited once.
- O(n) space — the set built per column holds at most n characters (one per string).
- Stopping at the first mismatch avoids unnecessary work on longer strings.

## 4. How It Works

Find the minimum-length word to bound the column scan. For each column index i, collect the character at position i from every string into a set. If the set has exactly one element all strings agree at that column and the character is appended to the prefix. The moment the set has more than one element the scan stops.

```python
min_len = min(len(x) for x in strs)
prefix = ""
for i in range(min_len):
    if len(set(x[i] for x in strs)) == 1:
        prefix += strs[0][i]
    else:
        break
return prefix
```

The set-size check is the key insight: instead of comparing each string to a reference string, collapsing all characters at a column into a set and checking its length handles the "all equal" condition in one step.

Input: `strs = ["flower","flow","flight"]`, `min_len = 4`

| i | chars at col i | set | size==1? | prefix |
|---|----------------|-----|----------|--------|
| 0 | f, f, f | {f} | yes | "f" |
| 1 | l, l, l | {l} | yes | "fl" |
| 2 | o, o, i | {o,i} | no → break | "fl" |
