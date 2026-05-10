class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        previous = prices[0]
        for curr in prices[1:]:
            if curr > previous:
                total += curr - previous
            previous = curr
        return total
