class Solution(object):
    def maxProfit(self, prices):
        bought_index = 0
        sold_index = 1
        max_profit = 0  # no profit possible

        while sold_index < len(prices):
            current_profit = prices[sold_index] - prices[bought_index]
            if prices[bought_index] < prices[sold_index]:
                max_profit = max(current_profit, max_profit)
            else:
                bought_index = sold_index
            sold_index += 1
        return max_profit


