# 219. Contains Duplicate II

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/contains-duplicate-ii/

## 1. Algorithm Used

Fixed-size sliding window of size `k` backed by a hash set to detect duplicates within the window.

## 2. How to Recognize the Pattern

- "two indices `i` and `j` such that `|i - j| <= k`" → fixed-size window of width `k` → slide and maintain a set.
- Duplicate detection within a bounded range → hash set membership check in O(1).
- Window size is given explicitly by the constraint `k` → no shrink condition needed, just evict the element that falls out of range.

## 3. Why This Algorithm Fits

- O(n) time — each element is added and removed from the set at most once.
- O(k) space — the set holds at most `k` elements at any time.
- A set (rather than a map) is sufficient because we only need to know whether a value exists in the window, not its exact index.

## 4. How It Works

We maintain a sliding set of the last `k` elements. Before adding `nums[i]` to the set, we check if it's already present — if so, a duplicate within distance `k` exists and we return `True`. After adding, if the set exceeds size `k` we evict the element that just left the window (`nums[i - k]`).

```python
window = set()
for i in range(len(nums)):
    if nums[i] in window:
        return True
    window.add(nums[i])
    if len(window) > k:
        window.remove(nums[i-k])
return False
```

The eviction condition `len(window) > k` (rather than `>= k`) ensures the window always contains exactly the `k` most recent elements before the next iteration's membership check.

Input: `nums = [1, 2, 3, 1]`, `k = 3`

| i | nums[i] | in window? | action | window |
|---|---------|------------|--------|--------|
| 0 | 1 | no | add | {1} |
| 1 | 2 | no | add | {1,2} |
| 2 | 3 | no | add | {1,2,3} |
| 3 | 1 | yes | return True | |
