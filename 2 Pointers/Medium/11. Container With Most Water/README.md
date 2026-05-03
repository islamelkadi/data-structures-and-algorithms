## 1. Algorithm Used

Two-pointer greedy shrink from both ends.

## 2. How to Recognize the Pattern

- Maximize area between two lines → depends on two variables: width (distance) and height (shorter line).
- Starting at maximum width and shrinking inward lets you explore all promising pairs.
- Brute force is O(n²). When you can eliminate candidates by moving one pointer at a time based on a greedy choice, think two pointers.

## 3. Why This Algorithm Fits

- Moving the pointer at the shorter line is the only move that could increase area — the taller line is never the bottleneck, so keeping it gives the best chance of finding a taller partner.
- Moving the taller side would only shrink width with no possibility of gaining height.
- This greedy elimination guarantees you never skip a potential maximum.

## 4. How It Works

Start with pointers at both ends (maximum width). Compute the area using the shorter height × distance. Move the pointer pointing to the shorter line inward. Repeat until the pointers meet. Track the largest area seen.

```python
largest_area = 0
left, right = 0, len(height) - 1
while left < right:
    lower_height = min(height[left], height[right])
    length = right - left
    area = lower_height * length
    largest_area = max(largest_area, area)
    if height[left] > height[right]:
        right -= 1
    else:
        left += 1
return largest_area
```

## 5. Time & Space Complexity

Time: O(n) — each iteration moves one pointer inward, so at most n - 1 iterations total.

Space: O(1) — only a few variables, no extra data structures.