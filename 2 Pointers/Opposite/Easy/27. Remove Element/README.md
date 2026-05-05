# 27. Remove Element
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/remove-element/

## 1. Algorithm Used

Opposite-direction two pointers (swap-to-back partition).

## 2. How to Recognize the Pattern

- "Remove all occurrences of val in-place" → partition the array so non-val elements are at the front.
- O(1) space constraint rules out a new array.
- Two approaches work: read/write same-direction (like #26), or opposite-direction swap. The swap approach is better here because order doesn't need to be preserved — swapping val elements to the back is enough.

## 3. Why This Algorithm Fits

- O(n) time — left and right together traverse the array at most once.
- O(1) space — only two index variables.
- Swapping instead of shifting avoids moving every element when val appears early — fewer writes overall.

## 4. How It Works

`right` starts at the end and retreats past any trailing `val` elements first. `left` scans forward. When `left > right`, all elements have been accounted for — break. When `nums[left] == val`, swap it with `nums[right]` (which is guaranteed non-val) and retreat `right`. Otherwise `left` just advances.

```python
right = len(nums) - 1
for left in range(len(nums)):
    while nums[right] == val and right >= 0:
        right -= 1
    if left > right:
        break
    if nums[left] == val:
        nums[left], nums[right] = nums[right], nums[left]
        right -= 1
return right + 1
```

The break condition is `left > right`, not `left == right`, because with an even-length array the pointers can cross without ever being equal — using `==` would miss that case.

Input: `nums = [3, 2, 2, 3]`, `val = 3`

| step | left | right | nums[left] | nums[right] | action |
|------|------|-------|------------|-------------|--------|
| init | 0 | 3 | 3 | 3 | right retreats past trailing 3s |
| 1 | 0 | 1 | 3 | 2 | nums[left]==val → swap → [2,2,3,3], right=1 |
| 2 | 1 | 1 | — | — | left > right → break |
| result | — | — | — | — | return right+1 = 2 |
