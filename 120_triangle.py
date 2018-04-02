class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        '''
        # top-down, space O(n*n/2)
        if not triangle:
            return 0
        m = len(triangle)
        n = len(triangle[-1])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
        
        for i in range(1, m):
            # 三角形，只需要计算当前col的长度
            n1 = len(triangle[i])
            for j in range(1, n1):
                if j == n1-1:
                    # 如果是每行的最后一列，只有一条路径通向它，即i-1,j-1
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        # 因为要最短路径，所以看最后一行的最小值
        return min(dp[-1])
        '''
    
        # down-top, space O(n)
        if not triangle:
            return 0
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
        