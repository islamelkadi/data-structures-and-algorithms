# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## 1. Algorithm Used

Sliding window with min-price tracking — `left` marks the cheapest buy day seen so far, `right` scans for the best sell day.

## 2. How to Recognize the Pattern

- "maximize profit" over a price array → need to track a running minimum → sliding window with two pointers.
- Only one buy and one sell allowed → no need for DP; a single left/right scan suffices.
- Profit depends on the difference between two elements where order matters (buy before sell) → left pointer never moves right of right pointer.

## 3. Why This Algorithm Fits

- O(n) time — single left-to-right pass through the array.
- O(1) space — only three integer variables maintained.
- The key property: if `prices[right] < prices[left]`, the current left can never be part of an optimal pair, so we move left to right and continue scanning.

## 4. How It Works

`left` starts at index 0 as the candidate buy day. For each `right`, we compute the profit of selling today. If `prices[right]` is cheaper than `prices[left]`, we've found a better buy day and slide `left` forward to `right`. We track the running maximum profit across all valid pairs.

```python
left = current_profit = max_profit = 0
for right in range(len(prices)):
    if prices[right] < prices[left]:
        left = right
    current_profit = prices[right] - prices[left]
    max_profit = max(max_profit, current_profit)
return max_profit
```

The window never needs to shrink from the right — we only ever move `left` forward when we find a strictly cheaper price, which guarantees we always hold the best possible buy day.
