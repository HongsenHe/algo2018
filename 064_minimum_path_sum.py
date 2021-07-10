class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for __ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        # 初始化第一列的每一行，即上一行的结果dp[i-1][0] 加上grid里面的数字
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # 初始化第一行的每一列，即前一列的结果dp[0][j-1] 加上grid里面的数字
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]
        