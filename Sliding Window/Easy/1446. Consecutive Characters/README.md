# 1446. Consecutive Characters

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/consecutive-characters/

## 1. Algorithm Used

Variable sliding window that expands while the character matches and resets `left` to `right` on a mismatch.

## 2. How to Recognize the Pattern

- "longest consecutive run of the same character" → contiguous subarray/substring constraint → sliding window.
- Window validity is a single equality check (`s[right] == s[left]`) → no auxiliary data structure needed.
- Reset-on-mismatch pattern: when the window breaks, the new window starts exactly at `right`, not `left + 1`.

## 3. Why This Algorithm Fits

- O(n) time — single pass through the string.
- O(1) space — only two pointers and an answer variable.
- Because all characters in a valid window are identical, comparing `s[right]` to `s[left]` is equivalent to comparing to any element in the window.

## 4. How It Works

`left` marks the start of the current run. For each `right` starting at index 1, if `s[right]` matches `s[left]` the window grows and we update the answer. If it doesn't match, the current run is broken and `left` jumps to `right` to begin a fresh run of length 1.

```python
left = 0; ans = 1
for right in range(1, len(s)):
    if s[right] == s[left]:
        ans = max(ans, right - left + 1)
    else:
        left = right
return ans
```

Initialising `ans = 1` handles the edge case of a single-character string without any special-casing after the loop.
