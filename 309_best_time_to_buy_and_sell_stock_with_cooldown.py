class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        思路：
        今天卖不卖，今天买不买的问题。。。（不要预测股市）
        sell[i] 表示第i天 有!   股票获得的最大利润
        buy[i]  表示第i天 没有  股票获得的最大利润
        
        1. 今天想买：要追溯前天卖的状态，sell[i-2] 再减去今天的买单 prices[i]
        2. 今天不想买：要看昨儿的状态，buy[i-1]
        3. 今天想卖：意味着昨天买的状态加上今天的价格（想卖看今天涨多少）
        4. 今天不想卖：要看昨儿的状态，sell[i-1]
        取1&2， 3&4的最大值
        
        看最后一天结束的时候，手里没有股票的最大利润 sell[n-1]
        '''
        
        if not prices or len(prices) < 2:
            return 0
        
        # init
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        buy[0] = -prices[0]
        buy[1] = max(buy[0], 0-prices[1]) # 0 is sell[i-2]
        sell[1] = max(0, prices[1] - prices[0])
        
        for i in range(2, n):
            buy[i] = max(sell[i-2] - prices[i], buy[i-1])
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])
        return sell[n-1]