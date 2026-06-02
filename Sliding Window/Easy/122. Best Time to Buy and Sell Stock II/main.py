class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # First attempt
        # padded_prices = [prices[0]] + prices
        # diff_padded_prices = []
        # for i in range(1, len(padded_prices)):
        #     diff_padded_prices.append(padded_prices[i] - padded_prices[i - 1])
        
        # summation = 0
        # for num in diff_padded_prices:
        #     if num > 0:
        #         summation += num
        # return summation

        # # Second attempt
        # summation = 0
        # for i in range(1, len(prices)):
        #     diff = prices[i] - prices[i - 1]
        #     if diff > 0:
        #         summation += diff
        # return summation

        # Alternative approach
        total = 0
        previous = prices[0]
        for curr in prices[1:]:
            if curr > previous:
                total += curr - previous
            previous = curr
        return total
