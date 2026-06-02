from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_hashset = set(jewels)
        stones_hashmap = Counter(stones)
        summation = 0
        for jewel in jewels_hashset:
            summation += stones_hashmap.get(jewel, 0)
        return summation
