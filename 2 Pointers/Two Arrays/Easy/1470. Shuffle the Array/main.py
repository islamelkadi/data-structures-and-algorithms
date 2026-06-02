from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new = []
        for i in range(n):
            new += ([nums[i], nums[i+n]])
        return new
