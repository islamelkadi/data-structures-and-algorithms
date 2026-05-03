from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        return sum(1 for x in arr if x + 1 in s)
