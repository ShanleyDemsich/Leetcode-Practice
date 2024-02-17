class Solution(object):
    def maxProfit(self, prices):
        profits_dict = {}
        for index, price in enumerate(prices):
            profits = set()
            for i in range(index, len(prices)):
                profits.add(prices[i] - price)
            profits_dict[price] = max(profits)

        if max(profits_dict, key=profits_dict.get) < 0:
            return 0  # no profit made
        return max(profits_dict)


