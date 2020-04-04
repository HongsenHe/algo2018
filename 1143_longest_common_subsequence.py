class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        table = [[0 for i in range(n)] for i in range(m)]
        
        '''
        经典DP题，判断两个字符的当前字符 text1[i]和 text2[j]
        如果相等，那就是1 + table矩阵i-1, j-1，也就是斜上方的结果
        如果不等，就要看如果拿掉当前字符i 即i-1 和拿到当前字符j 即j-1
                的结果，看看哪个方案更大
        table 矩阵最后一个数就是答案了。
        table需要包含空字符，建立的时候需要m+1, n+1, 运行的时候需要从1开始
        '''
        
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    table[i][j] = 1 + table[i-1][j-1]
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        return table[m-1][n-1]