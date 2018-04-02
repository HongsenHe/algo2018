class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        '''
        如果没栅栏就不玩了。。。
        当前的栅栏i是什么颜色取决于 i-1和i-2 栅栏的颜色。
        如果i-1和i-2颜色一样：
            那当前颜色必须不一样，也就是当前栅栏i有k-1种选择，再乘以i-1也就是i-2的种类
            (k-1) x dp[i-1]
        如果i-1和i-2颜色不一样：
            那当前颜色可以和i-1一样，也可以和i-1不一样。
            如果和i-1一样：
                就有k-1种选择, 另一个是i-2的颜色. 现在i和i-1一个颜色，而不能和i-2一个颜色
                所以，有k-1种选择并且乘以dp[i-2]，看看i-2有多少种解法，（k-1) x dp[i-2]
            如果和i-1不一样：
                还是有k-1种选择，再乘以i-1所有的种类 (k-1) x dp[i-1]
        综上：dp[i] = (k-1) x dp[i-1] + (k-1) x dp[i-2] = (k-1) x (dp[i-1] + dp[i-2])
        
        或者说：看当前和前面的一个：
        如果不同：
            那就当前的选择 X 前一个的结果： (k-1) x dp[i-1]
        如果相同：
            那问题就转移到前面一个i-1和i-2的关系：
            因为他俩肯定不同，所以还是第一种情况：（k-1) x dp[i-2]
        综上： dp[i] = (k-1) x (dp[i-1] + dp[i-2])
        '''

        '''
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = k
        dp[2] = k*k
        for i in range(3, n+1):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])
        return dp[n]
        '''
    
        '''
        #优化版
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        prev2 = k
        prev = k * k
        cur = 0
        for i in range(3, n+1):
            cur = (k-1) * (prev + prev2)
            prev2 = prev
            prev = cur
        return cur
        '''
        
        '''
        另一种思路 不用DP
        对于当前的栅栏，看和前面的一个颜色是不是相同？
        1. 如果和前面栅栏颜色不同，有多少种玩法？
            当前有k-1种玩法，再乘以之前所有的玩法total
            即，不同 diff = (k-1) x total
        2. 如果和前面栅栏颜色相同，有多少种玩法？那就看前面和前前面的关系喽。
            i和i-1相同，i, i-1, i-2又不能都相同，所以i-1和i-2不能相同
            并且有diff种玩法。
            即，相同 same = diff
        最后一共多少种 即, total = same + diff
        '''
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        same = 0
        diff = k
        total = k
        for i in range(2, n+1):
            same = diff
            diff = (k-1) * total
            total = same + diff
        return total
