class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        '''
        dp[i] 表示字符串前i位解码有多少种方式
        初始化: dp[0] = dp[1] = 1， 其他均为0
        
        数字226178
        对于当前i=2 (6) 
        如果前面两个数字i-2在10-26，即把i-2的答案加入到当前结果里
        继续判断如果前面一个数字i-1在1-9，即把i-1的答案集合放到结果dp[i]里
        如果都不是，（优化部分不是必须）则返回0
        step by step 最后返回dp的最后一个数字即答案。累加爬梯子的概念。
        '''
        
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            dp.append(0)
            
            # s[i-2] 和 s[i-1] 表示10-26数字
            if 10 <= int(s[i-2 : i]) <= 26:
                dp[i] += dp[i-2]
            
            # s[i-1] 表示 1-9数字
            if 1 <= int(s[i-1 : i]) <= 9:
                dp[i] += dp[i-1]
                
            # 优化部分，都不是直接返回答案0
            if dp[i] == 0:
                return 0
            
        return dp[len(s)]