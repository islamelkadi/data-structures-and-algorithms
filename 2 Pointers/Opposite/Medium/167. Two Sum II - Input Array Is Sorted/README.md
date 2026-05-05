# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## 1. Algorithm Used

Opposite-direction two pointers on a sorted array: converge based on whether the current sum is below or above the target.

## 2. How to Recognize the Pattern

- "Sorted array, find two numbers that sum to target" → sorted input enables two-pointer convergence → no hash map needed.
- Exactly one solution is guaranteed → the pointers will always find it before crossing.
- 1-indexed output required → add 1 to both pointer values before returning.

## 3. Why This Algorithm Fits

- O(n) time — each pointer moves at most n steps total; they never backtrack.
- O(1) space — only two integer pointers, no auxiliary data structure.
- The sorted order is the key invariant: if the sum is too small, the only way to increase it is to advance `left`; if too large, the only way to decrease it is to retreat `right`.

## 4. How It Works

Place `left` at index 0 and `right` at the last index. Compute `numbers[left] + numbers[right]`. If the sum is less than `target`, advance `left` to get a larger value. If greater, retreat `right` to get a smaller value. When the sum equals `target`, return `[left + 1, right + 1]` (1-indexed).

```python
left = 0
right = len(numbers) - 1
while left < right:
    summation = numbers[left] + numbers[right]
    if summation < target:
        left += 1
    elif summation > target:
        right -= 1
    else:
        return [left + 1, right + 1]
```

Because exactly one solution is guaranteed, the loop will always hit the `else` branch before `left` and `right` cross — no need for a fallback return.

Input: `numbers = [2, 7, 11, 15]`, `target = 9`

| left | right | numbers[left] | numbers[right] | sum | action |
|------|-------|---------------|----------------|-----|--------|
| 0 | 3 | 2 | 15 | 17 | >target → right-- |
| 0 | 2 | 2 | 11 | 13 | >target → right-- |
| 0 | 1 | 2 | 7 | 9 | ==target → return [1, 2] |
