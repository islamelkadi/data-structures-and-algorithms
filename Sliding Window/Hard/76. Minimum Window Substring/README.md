# 76. Minimum Window Substring

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/minimum-window-substring/

## 1. Algorithm Used

Variable sliding window with two character-frequency hashmaps and a `curr` counter that tracks how many characters of `t` are currently satisfied by the window.

## 2. How to Recognize the Pattern

- "minimum window in `s` that contains all characters of `t`" → find smallest valid subarray → shrink-when-valid sliding window.
- Must contain all characters with correct frequencies → need a frequency map for `t` and a running map for the window.
- "Satisfied requirement" counting (`curr`) avoids re-scanning the entire map on every step — a classic optimisation for multi-character window problems.

## 3. Why This Algorithm Fits

- O(|s| + |t|) time — each character in `s` is added and removed at most once; building `t_hashmap` is O(|t|).
- O(|t|) space — both hashmaps are bounded by the number of distinct characters in `t`.
- The `curr == len(t)` condition is a O(1) validity check because `curr` is maintained incrementally rather than recomputed each iteration.

## 4. How It Works

We build `t_hashmap` from `t` upfront. As `right` expands, we increment `s_hashmap[s[right]]` and increment `curr` only when the new count exactly meets (not exceeds) the required count — this prevents over-counting. Once `curr == len(t)` the window is valid: we record it if it's the smallest seen, then shrink from `left`, decrementing `curr` only when removing a character drops its count below the required threshold.

```python
t_hashmap = Counter(t)
s_hashmap = defaultdict(int)
curr = left = left_boundary = 0; ans = float("inf")
for right in range(len(s)):
    if s[right] in t_hashmap:
        s_hashmap[s[right]] += 1
        if s_hashmap[s[right]] <= t_hashmap[s[right]]:
            curr += 1
    while curr == len(t):
        if right - left + 1 < ans:
            ans = right - left + 1; left_boundary = left
        if s[left] in s_hashmap:
            s_hashmap[s[left]] -= 1
            if s_hashmap[s[left]] < t_hashmap[s[left]]:
                curr -= 1
        left += 1
```

The `<=` / `<` asymmetry is the key insight: `curr` only changes at the exact threshold, so extra copies of a character in the window don't inflate or deflate the satisfaction count.
