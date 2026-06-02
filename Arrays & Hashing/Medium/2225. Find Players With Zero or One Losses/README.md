# 2225. Find Players With Zero or One Losses
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/find-players-with-zero-or-one-losses/


## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)

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

Input: `matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]`

| match | winner | loser | losses map update |
|-------|--------|-------|-------------------|
| [1,3] | 1 | 3 | {1:0, 3:1} |
| [2,3] | 2 | 3 | {1:0, 2:0, 3:2} |
| [3,6] | 3 | 6 | {1:0, 2:0, 3:2, 6:1} |
| [5,6] | 5 | 6 | {…, 5:0, 6:2} |
| [5,7] | 5 | 7 | {…, 7:1} |
| [4,5] | 4 | 5 | {…, 4:0, 5:1} |
| [4,8] | 4 | 8 | {…, 8:1} |
| [4,9] | 4 | 9 | {…, 9:1} |
| [10,4] | 10 | 4 | {…, 10:0, 4:1} |
| [10,9] | 10 | 9 | {…, 9:2} |
| no_loss | | | [1, 2, 10] (losses==0) |
| one_loss | | | [4, 5, 7, 8] (losses==1) |
