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
