# 340. Longest Substring with At Most K Distinct Characters

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

## 1. Algorithm Used

Variable sliding window with a character-frequency map that shrinks from the left whenever the number of distinct characters exceeds `k`.

## 2. How to Recognize the Pattern

- "at most k distinct characters" → bounded-diversity window → sliding window with a frequency map.
- Window validity is `len(counts) <= k` → shrink when violated, expand otherwise.
- Delete the key entirely when its count reaches 0 — this keeps `len(counts)` as an accurate distinct-character count without a separate set.

## 3. Why This Algorithm Fits

- O(n) time — each character is added and removed from the map at most once.
- O(k) space — the map holds at most `k + 1` keys before shrinking kicks in.
- Using a `defaultdict` and deleting zero-count keys is cleaner than a regular dict with existence checks, and avoids off-by-one errors in the distinct count.

## 4. How It Works

For each `right`, we increment `counts[s[right]]`. If the number of distinct keys exceeds `k`, we shrink from `left`: decrement `counts[s[left]]`, delete the key if it hits 0 (removing it from the distinct count), then advance `left`. Once the window is valid again we update the maximum length.

```python
counts = defaultdict(int); left = ans = 0
for right in range(len(s)):
    counts[s[right]] += 1
    while len(counts) > k:
        counts[s[left]] -= 1
        if counts[s[left]] == 0: del counts[s[left]]
        left += 1
    ans = max(ans, right - left + 1)
return ans
```

The `del` on zero-count is the critical step — without it `len(counts)` would never decrease and the shrink loop would run forever.
