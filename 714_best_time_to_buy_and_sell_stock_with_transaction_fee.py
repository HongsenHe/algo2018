class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        '''
        卖还是保留？
        如果卖，看昨天有股票的利润加上今天的价格减去手续费
        和昨天卖的利润相比，如果昨天利润比较大，就昨天卖了，不留了。
        sell[i] = max(sell[i-1], hold[i-1] + prices[i] - fee)
        如果保留，看昨天卖的利润减去今天买的价格
        和如果昨天保留相比，如果昨天保留利润大，今天继续保留
        hold[i] = max(hold[i-1], sell[i-1] - prices[i])
        
        其实至于昨天有关系所以：
        sell[i] = max(sell[i-1], hold[i-1] + prices[i] - fee)
        hold[i] = max(hold[i-1], sell[i-1] - prices[i])
        可以变成：
        sell = max(sell, hold + today_price - fee)
        hold = max(hold, sell - prices[i])
        
        '''
        
        if len(prices) < 2:
            return 0
        
        sell = 0
        hold = -prices[0] # 如果只保留，最终还是赔钱
        
        for i in range(1, len(prices)):
            sell = max(sell, hold + prices[i] - fee)
            hold = max(hold, sell - prices[i])
        return sell
