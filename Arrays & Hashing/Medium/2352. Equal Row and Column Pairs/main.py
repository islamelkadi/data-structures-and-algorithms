from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counts = Counter(tuple(row) for row in grid)
        count = 0
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            count += row_counts[col_tuple]
        return count
