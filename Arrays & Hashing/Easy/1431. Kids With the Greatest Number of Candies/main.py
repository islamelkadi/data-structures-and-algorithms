from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_no_extras = max(candies)
        max_candies = [False] * len(candies)
        for i, kid_candy in enumerate(candies):
            if (kid_candy + extraCandies) >= max_no_extras:
                max_candies[i] = True
        return max_candies
