# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Sliding window with min-price tracking — `left` marks the cheapest buy day seen so far, `right` scans for the best sell day.

## 2. How to Recognize the Pattern

- **Maximize profit over a price array**: Need to track a running minimum, suggesting a sliding window with two pointers.
- **Only one buy and one sell allowed**: No need for complex dynamic programming; a single pass is sufficient.
- **Order-dependent differences (buy before sell)**: The `left` pointer never moves to the right of the `right` pointer.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Single left-to-right pass through the array.
- **$O(1)$ space**: Only a few integer variables are maintained.
- **Optimal substructure**: If `prices[right] < prices[left]`, the current `left` can never be part of a better transaction than what we could find using `right` as the new buy date. Thus, we safely slide `left` to `right`.

## 4. How It Works

`left` starts at index 0 as the candidate buy day. For each `right` from 0 to the end:
1. If `prices[right]` is cheaper than `prices[left]`, we've found a better buy day, so we slide `left` forward to `right`.
2. We compute the current profit (`prices[right] - prices[left]`) and update the `max_profit`.

```python
# SLIDING WINDOW
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Can this be done in a single shot O(N) and Space Complexity of O(1)
        # Curr represents current max profit known of
        # Ans represent the latest max profit discovered after full iteration
        left = current_profit = max_profit = 0

        # Initialize min price
        for right in range(len(prices)):

            # Mechanism to point to the correct min price
            if prices[right] < prices[left]:
                left = right
            
            # Calculate profits and keep record of highest
            # selling day point
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)

        return max_profit
```

### Dry Run Table
Input: `prices = [7, 1, 5, 3, 6, 4]`

| right | prices[right] | prices[left] | left | current_profit | max_profit |
|---|---|---|---|---|---|
| 0 | 7 | 7 | 0 | 0 | 0 |
| 1 | 1 | 7 | 1 | 0 | 0 |
| 2 | 5 | 1 | 1 | 4 | 4 |
| 3 | 3 | 1 | 1 | 2 | 4 |
| 4 | 6 | 1 | 1 | 5 | 5 |
| 5 | 4 | 1 | 1 | 3 | 5 |

Result: `5`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the length of `prices`. We traverse the array exactly once.
- **Space Complexity**: $O(1)$ since we only use constant auxiliary variables.
