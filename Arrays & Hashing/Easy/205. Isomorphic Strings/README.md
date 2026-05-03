# 205. Isomorphic Strings
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/isomorphic-strings/

## 1. Algorithm Used

Bidirectional character mapping using two hashmaps to enforce a strict one-to-one correspondence.

## 2. How to Recognize the Pattern

- "replace characters to transform one string into another" → need a consistent mapping → hashmap.
- The mapping must be injective (no two source characters map to the same target) → a single forward map is not enough → add a reverse map.
- Any conflict in either direction means the strings are not isomorphic.

## 3. Why This Algorithm Fits

- O(n) time — a single pass through both strings.
- O(1) space — the maps hold at most 26 entries each for lowercase ASCII.
- Two maps together enforce bijectivity without sorting or extra passes.

## 4. How It Works

Iterate through paired characters `(s[i], t[i])`. For each pair, check whether `s[i]` already maps to a different character in `t`, or whether `t[i]` already maps back to a different character in `s`. Either conflict returns False immediately. Otherwise both mappings are recorded.

```python
s_hashmap, t_hashmap = {}, {}
for i in range(len(s)):
    if s[i] in s_hashmap and s_hashmap[s[i]] != t[i]:
        return False
    if t[i] in t_hashmap and t_hashmap[t[i]] != s[i]:
        return False
    s_hashmap[s[i]] = t[i]
    t_hashmap[t[i]] = s[i]
return True
```

The reverse map `t_hashmap` is what prevents two different source characters from collapsing onto the same target character — a check the forward map alone cannot catch.
