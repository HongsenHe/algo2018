class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix) + 1
        n = len(matrix[0]) + 1
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        '''
        定义dp[i][j]就是正方形右下角的边长数值，每次更新并且与最大值比较，
        最后返回最大值res * res
        
        前提条件是当前node matrix[i-1][j-1] 是'1'：
        右下角与上，左，左上的结果有关，也是DP的关键，用mxn来保存之前结果
        要保证是正方形，所以木桶效应需要找到最短的木版，也就是找这三个位置的最小数值
        并且加上本身 即:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        
        '''
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    res = max(res, dp[i][j])
        return res * res