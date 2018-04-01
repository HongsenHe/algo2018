class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        '''
        用三个dp 表示不同颜色，不同房间，比如
        dp[i][0] 表示刷第i个房子，用红色，所以要看前面房子蓝色和绿色的花费，即
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        最后看哪个dp的值最小，即看哪个路径值最小
        '''
        
        '''
        if not costs or len(costs) == 0:
            return 0
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        # dp[0][0] = costs[0][0]
        # dp[0][1] = costs[0][1]
        # dp[0][2] = costs[0][2]
        dp[0] = costs[0]
        
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        return min(dp[-1])
        '''
        
    
        '''
        或者只保存当前最优解，只需要一个list, 分别保存三种颜色的最优解
        '''
        if not costs or len(costs) == 0:
            return 0
        dp = costs[0]
        for i in range(1, len(costs)):
            tmp = dp[:] # 先保存之前的状态，接下来要被改变
            dp[0] = min(tmp[1], tmp[2]) + costs[i][0]
            dp[1] = min(tmp[0], tmp[2]) + costs[i][1]
            dp[2] = min(tmp[0], tmp[1]) + costs[i][2]
        return min(dp)