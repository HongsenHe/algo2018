class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        DP的O(n2)解法
        dp[i] 代表以nums[i]这个数结尾的最长递增子串的长度
        对于每一个nums[i] 从起始点开始搜索到i 
        如果发现某个数字dp[j] 小于 nums[i] 就更新dp[i], 方法是：
        dp[i] = max(dp[i], dp[j]+1) 
        比如[2, 5, 3, 7] nums[i] 当前是数字是7， 从2开始搜索，
        发现2<7, 则看dp[2]的长度加上1 （当前数字的长度）
        
        然后当前轮dp[i]再和全局的结果比较，取大 
        res = max(dp[i], res)
        '''
        res = 0
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
        	for j in range(i):
        		if nums[j] < nums[i]:
        			dp[i] = max(dp[i], dp[j]+1)
        	res = max(dp[i], res)
        return res
                
                
                
        