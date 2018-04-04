class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        # dp[i][j] 表示从word1的i字符到word2的j字符的最短距离
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        # 初始化的时候，比如第一列，dp[i][0]那就是word1的i字符到word2的j字符
        # 转换长度，也就是编辑距离，随着i增加而增加，因此设置为i。列同理。
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 如果word1 word2之前的字符相等，用前面的关系
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    '''
                    重点来啦，如果当前字符不相等，有三种情况，增加删除修改
                    
                    增加：a和ab 是word1要增加一个字符'b' 才等于word2 'ab'
                    dp[i][j] = dp[i][j-1] + 1, dp[i][j-1]表示，word2减去当前的字符之后，
                    和word1的关系, 1表示当前的增加操作
                        
                    删除：ab和a 是word1要减少一个字符'b' 才等于word2 'a'
                    dp[i][j] = dp[i-1][j] + 1, dp[i-1][j] 表示word1减少当前字符之后，
                    与word2的关系，1表示当前的删除操作
                    
                    替换：ab和ac 是word1要把'b' 换成'c' 才等于word2 'ac'
                    dp[i][j] = dp[i-1][j-1] + 1, dp[i-1][j-1] 表示word1减少当前字符，
                    word2也减少当前字符之后，他们的关系，1表示当前的操作。
                    
                    这三种情况选择最小的方案 作为当前的方案
                    '''
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[m][n]