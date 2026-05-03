# 2225. Find Players With Zero or One Losses
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/find-players-with-zero-or-one-losses/

## 1. Algorithm Used

Loss frequency tracking with a defaultdict — count losses per player, then filter by loss count.

## 2. How to Recognize the Pattern

- "track a count per entity across a list of events" → defaultdict or Counter → filter by threshold.
- Winners who never appear as a loser must still be registered — initialize them explicitly.

## 3. Why This Algorithm Fits

- O(n log n) time — O(n) to build the loss map, O(k log k) to sort the results.
- O(k) space — k is the number of unique players.
- defaultdict avoids KeyError when a winner has never lost.

## 4. How It Works

Iterate through matches. For each winner, ensure they appear in the losses map with 0 if not already present. For each loser, increment their loss count. Then filter and sort players by their loss count.

```python
from typing import List
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[loser] += 1
        no_loss = sorted(p for p, l in losses.items() if l == 0)
        one_loss = sorted(p for p, l in losses.items() if l == 1)
        return [no_loss, one_loss]
```

The explicit `if winner not in losses: losses[winner] = 0` is the key detail — a player who only wins never appears as a loser, so they'd be missed without this initialization.
