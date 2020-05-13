class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        if len(nums) < 3:
            return max(nums)
        
        '''
        现在面临的问题是个圆形：对于第一家和最后一家只能抢一个。
        于是算两遍：1. 抢第一家放弃最后一家，2. 抢最后一家，放弃第一家。
        还是一样的方法，放人不同的两种情况算算，取最大值。
        '''
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums):
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]