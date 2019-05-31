class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        '''
        三种操作：买，卖，休，分别DP一下
        1. 买的前一个操作是休息，如果真买了，利润要减去买入价格也就是当天价格
        buy[i] = max(res[i-1]-price, buy[i-1]) 比较买还是不买
        2. 卖的前一个操作是买，如果真卖了，利润要加上当天价格
        sell[i] = max(buy[i-1]+price, sell[i-1]) 比较卖还是不卖
        3. 休息的前一个操作可以是买，卖或休息
        rest[i] = max(buy[i-1], sell[i-1], rest[i-1])
        但如果买收益肯定小于休息收益，也小于卖的收益。
        即：buy[i] <= rest[i] <= sell[i]
        上述方程就是：rest[i] = sell[i-1]

        代入 1 2 方程即：
        buy[i] = max(sell[i-2]-price, buy[i-1])
        sell[i] = max(buy[i-1]+price, sell[i-1])

        代码如下：
        '''
        
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        
        '''
        buy[i] = max(sell[i-2]-price, buy[i-1])
        sell[i] = max(buy[i-1]+price, sell[i-1])
        '''
        buy[0] = -prices[0]
        buy[1] = max(0-prices[1], buy[0])
        sell[1] = max(buy[0]+prices[1], 0)
        
        for i in range(2, n):
            buy[i] = max(sell[i-2]-prices[i], buy[i-1])
            sell[i] = max(buy[i-1]+prices[i], sell[i-1])
            
        return max(buy[n-1], sell[n-1])



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
        '''


