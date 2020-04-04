class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        axbybza
        分析
        根据palindrome的特性就是头尾相等，dp[i][j] 表示 s[i...j]的结果
        如果s[i] == s[j] 结果就是里面的结果(i+1)和(j-1) + 2
            即： dp[i][j] = dp[i+1][j-1] + 2
        如果s[i] != s[j] 这样就各自[退一步] 看看s[i+1 ... j] (向下）
            和s[i ... j-1] （向左）的结果，然后取一个最大值，逐步建立起来结果matrix
            即： dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        顺序
        构建window长度分别从2到m的substring. 比如n = 3 计算axb, xby, byb, ybz, bza
        两个指针i, j: i就是从0到m-n, j就是从window的另一端即 i+n-1
        只需填满矩阵上右半部分，每次可以根据max(下，左) 和下左来赋值。
        '''
        m = len(s)
        dp = [[0 for _ in range(m)] for _ in range(m)]
        
        # 中间的或者奇数的就是自己 长度即1
        for i in range(m):
            dp[i][i] = 1
        
        for k in range(2, m+1):
            for i in range(m-k+1):
                j = i+k-1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
