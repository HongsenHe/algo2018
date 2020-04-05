class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                # 赚钱就跑的小散
                profit += prices[i] - prices[i-1]
        return profit


    # updated at 04052020
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = float('inf')
        profit = 0
        
        for price in prices:
            if price > buy:
                profit += price - buy
            buy = price
        return profit