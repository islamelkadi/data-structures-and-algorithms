# 485. Max Consecutive Ones

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/max-consecutive-ones/

## 1. Algorithm Used

Variable sliding window with a zero budget of 0 — the window shrinks whenever a zero is encountered, effectively counting only runs of ones.

## 2. How to Recognize the Pattern

- "maximum consecutive ones" in a binary array → contiguous subarray with a value constraint → sliding window.
- Zero budget of 0 means any zero immediately invalidates the window → shrink until the zero is expelled.
- This is the base case of the "max consecutive ones with at most k zeros" family (see 487 and 1004).

## 3. Why This Algorithm Fits

- O(n) time — each element is visited by `right` once and by `left` at most once.
- O(1) space — only three integer variables.
- Using a zero counter and a `while` shrink loop generalises cleanly to k-zero variants without restructuring the algorithm.

## 4. How It Works

`zero_counter` tracks how many zeros are inside the current window. When `nums[right]` is 0 the budget is exceeded immediately (budget = 0), so the `while` loop advances `left` until the zero is removed. After shrinking, the window `[left, right]` contains only ones and we update the maximum length.

```python
left = zero_counter = max_array_len = 0
for right in range(len(nums)):
    if nums[right] == 0:
        zero_counter += 1
    while zero_counter > 0:
        if nums[left] == 0:
            zero_counter -= 1
        left += 1
    max_array_len = max(max_array_len, right - left + 1)
return max_array_len
```

Writing this with an explicit `zero_counter` and `while` loop (rather than a simple `if nums[right] == 0: left = right + 1`) makes the pattern identical to the harder variants — changing the budget from 0 to 1 or k solves 487 and 1004 with no structural changes.
