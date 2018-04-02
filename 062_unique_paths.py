class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
    
        if m == 0 or n == 0:
            return 0
        
        # 学习这种方式初始化2D array, 一开始只有一种走法
        # dp = []
        # for i in range(m):
        #     col = []
        #     for j in range(n):
        #         col.append(1)
        #     dp.append(col)
        # 更PythonIC
        dp = [[1 for _ in range(n)] for _ in range(m)]
            
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]