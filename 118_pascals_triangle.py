class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [[1] * (i+1) for i in range(numRows)]
        for i in range(1, numRows):
            # current length is i
            for j in range(1, i):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp