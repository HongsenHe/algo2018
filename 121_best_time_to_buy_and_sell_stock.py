class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = float('inf')
        profit = 0
        for price in prices:
            if price < low:
                low = price
            profit = max(profit, price-low)
        return profit