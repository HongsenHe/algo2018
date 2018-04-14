class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        DP问题，先观察一下下：
        1. 如果n=0, 没节点那就是一个答案即空树！，dp[0] = 1
        2. 如果n=1, 有一个节点，那就是有一个答案root only， dp[1] = 1
        3. 如果n=2, 两种情况，root = 1 or root = 2
           1        2
            \      /
             2    1
        dp[2] = dp[0] * dp[1] (root = 1)
              + dp[1] * dp[0] (root = 2)
        4. 如果n=3, 三种情况，root = 1, root = 2 or root = 3
            1            1          2         3      3
             \            \        / \       /      /
              2            3      1   3     2      1
               \          /                /        \
                3        2                1          2
            
        dp[3] = dp[0] + dp[2] (root = 1, left-tree = 0 node, right-tree = 2 nodes)
              + dp[1] + dp[1] (root = 2, left-tree = 1 node, right-tree = 1 node)
              + dp[2] + dp[0] (root = 3, left-tree = 2 nodes, right-tree = 0 node)
              
        观察分析xxx 可以推断
        dp[i] = sum (dp[j] * dp[i-j-1]), j = [0, i)
        '''
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
        