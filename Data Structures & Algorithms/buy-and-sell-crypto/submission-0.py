class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lower_index = 0
        upper_index = 1

        while (upper_index < len(prices)):
            if (prices[lower_index] <= prices[upper_index]):
                max_profit = max(max_profit,prices[upper_index] - prices[lower_index])
                upper_index += 1
            elif prices[lower_index] > prices[upper_index]:
                lower_index = upper_index
                upper_index += 1
        return max_profit