class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        经典dp题！
        dp[n] 就是组成$n 需要的最少硬币，初始化需要amount+1个长度
        外循环是amount, 也就是对于每一个钱，dp的组合是什么
        核心方程式就是：
        dp[i] = min(dp[i], dp[i-coins[j]]+1)
        coins[j]就是当前使用的硬币，dp[i-coins[j]] 就是当前的钱数i减去这个硬币的方案加上他自己1
        和当前的答案比较，取小。
        '''
        inf = float('inf')
        dp = [0] + [inf]*amount
        for i in range(1, amount+1):
            if dp[i] < 0:
                continue
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        print(dp)
        if dp[amount] > amount:
            return -1
        return dp[amount]
