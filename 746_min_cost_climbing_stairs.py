class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        '''
        当前台阶只看之前两个台阶的花费，选小的一个，再加上当前, 
        看后两个哪个更小，因为都可以走到终点，用list 或者两个变量代替
        '''
        
        '''
        n = len(cost)
        if n < 3:
            return min(cost)
        
        price = [0] * n
        price[0] = cost[0]
        price[1] = cost[1]
        
        for i in range(2, n):
            price[i] = min(price[i-1], price[i-2]) + cost[i]
        return min(price[n-1], price[n-2])
        '''

        n = len(cost)
        if n < 3:
            return min(cost)
        prev2 = cost[0]
        prev1 = cost[1]
        for i in range(2, n):
            cur = min(prev2, prev1) + cost[i]
            prev2 = prev1
            prev1 = cur
        return min(prev2, prev1)