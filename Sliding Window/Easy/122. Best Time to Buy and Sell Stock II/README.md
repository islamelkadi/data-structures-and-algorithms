# 122. Best Time to Buy and Sell Stock II

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Greedy single pass — accumulate every upward price movement as profit.

## 2. How to Recognize the Pattern

- **Unlimited buy/sell transactions**: Capture every profitable day-to-day gain.
- **No cooldown or transaction limit**: No dynamic programming needed, just sum all positive consecutive differences.
- **Consecutive trading**: Buying and selling every consecutive profitable pair is mathematically equivalent to holding through any longer profitable run.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Single pass through the array.
- **$O(1)$ space**: Requires only two variables (`total` and `previous`).
- **Greedy approach works**: Since there are no transaction fees or trade frequency constraints, capturing every small positive increment guarantees the maximum possible total gain.

## 4. How It Works

Track the `previous` price. For each `curr` price:
1. If `curr` is greater than `previous`, add `curr - previous` to our total profit.
2. Update `previous = curr` at each step.

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # First attempt
        # padded_prices = [prices[0]] + prices
        # diff_padded_prices = []
        # for i in range(1, len(padded_prices)):
        #     diff_padded_prices.append(padded_prices[i] - padded_prices[i - 1])
        
        # summation = 0
        # for num in diff_padded_prices:
        #     if num > 0:
        #         summation += num
        # return summation

        # # Second attempt
        # summation = 0
        # for i in range(1, len(prices)):
        #     diff = prices[i] - prices[i - 1]
        #     if diff > 0:
        #         summation += diff
        # return summation

        # Alternative approach
        total = 0
        previous = prices[0]
        for curr in prices[1:]:
            if curr > previous:
                total += curr - previous
            previous = curr
        return total
```

### Dry Run Table
Input: `prices = [7, 1, 5, 3, 6, 4]`

| curr | previous | curr > prev? | profit added | total |
|---|---|---|---|---|
| 1 | 7 | no | 0 | 0 |
| 5 | 1 | yes | 4 | 4 |
| 3 | 5 | no | 0 | 4 |
| 6 | 3 | yes | 3 | 7 |
| 4 | 6 | no | 0 | 7 |

Result: `7`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of elements in `prices`. We perform a single traversal of the price history.
- **Space Complexity**: $O(1)$ auxiliary space as we only store `total` and `previous`.
