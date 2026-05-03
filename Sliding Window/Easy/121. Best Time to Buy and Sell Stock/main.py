class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Can this be done in a single shot O(N) and Space Complexity of O(1)
        # Curr represents current max profit known of
        # Ans represent the latest max profit discovered after full iteration
        left = current_profit = max_profit = 0

        # Initialize min price
        for right in range(len(prices)):

            # Mechanism to point to the correct min price
            if prices[right] < prices[left]:
                left = right
            
            # Calculate profits and keep record of highest
            # selling day point
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)

        return max_profit