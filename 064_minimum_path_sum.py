class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) + 1
        n = len(grid[0]) + 1
        
        # 初始化，size都加上1 形成一个外圈，并且附上初始值0
        dp = [[float('inf') for _ in range(n)] for __ in range(m)]
        dp[0][1] = 0
        dp[1][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[-1][-1]
        