## 1. Algorithm Used

Greedy single pass — accumulate every upward price movement as profit.

## 2. How to Recognize the Pattern

- "Unlimited buy/sell transactions" → capture every profitable day-to-day gain → greedy.
- No cooldown or transaction limit → no DP needed, just sum all positive differences.
- The key insight: buying and selling every consecutive profitable pair is equivalent to holding through any longer profitable run.

## 3. Why This Algorithm Fits

- O(n) time — single pass through prices.
- O(1) space — only two variables.
- Greedy works here because there are no constraints limiting when you can trade — every upward tick is free profit.

## 4. How It Works

Track the previous price. For each current price, if it's higher than the previous, add the difference to the total. Always update previous to current regardless.

```python
total = 0
previous = prices[0]
for curr in prices[1:]:
    if curr > previous:
        total += curr - previous
    previous = curr
return total
```

Input: `prices = [7, 1, 5, 3, 6, 4]`

| curr | previous | curr > prev? | profit added | total |
|------|----------|--------------|--------------|-------|
| 1 | 7 | no | 0 | 0 |
| 5 | 1 | yes | 4 | 4 |
| 3 | 5 | no | 0 | 4 |
| 6 | 3 | yes | 3 | 7 |
| 4 | 6 | no | 0 | 7 |

## 5. Time & Space Complexity

Time: O(n) — single pass.

Space: O(1) — two scalar variables.
