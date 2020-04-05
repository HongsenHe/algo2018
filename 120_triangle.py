class Solution:
    # updated 04042020
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        m = len(triangle)
        # 一开始初始化dp就是用三角形最后一行即dp = triangle[-1]
        dp = triangle[-1]
                
        for i in range(m-2, -1, -1):
            # 因为是三角形，j 只计算到本行末尾就好，虽然是个矩阵来模拟dp
            for j in range(len(triangle[i])):
                '''
                从下到上，每次都看当前行的下一行，只有两个即正下方（dp[j])
                和下右方 (dp[j+1])，取小的 加上当前行的数字triangle[i][j]
                就是当前行dp[j]的数值
                '''
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
        

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
        