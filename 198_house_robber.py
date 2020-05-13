class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        当前的屋子，你到底偷还是不偷？
        偷，意味着前面的你就不能偷，不能太贪是吧。但也要偷前面前面的， why not?
        不偷，你可以偷前面的。但不能偷前面前面的。然后取最大。
        
        不必N+1, 直接定义前两个，dp[0]肯定是第一个了
        dp[1]要看第一个房子nums[0]和nums[1]哪个大用哪个
        之后的for loop就从第三个房子nums[2]开始，递归式不变
        '''
        
        # Space O(n)
        if not nums or len(nums) == 0:
            return 0
        
        if len(nums) < 3:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]
            
        
        '''
        # Space O(1)
        if not nums:
            return 0
        prev2 = 0 # 没房子
        prev1 = nums[0] # 第一家房子
        
        for i in range(1, len(nums)):
            cur = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = cur
        return prev1 # 到最后prev1 = cur, 也就是偷到最后一个房子开始数钱啦
        '''
        

    
        '''
        换一种思路，当前的房子你是偷还是不偷，搞两个变量，taken, nonTaken
        偷：这家的财产加上之前不偷的总和，taken = nums[i] + nonTaken
        不偷：当天就是最大利润，nonTaken = maxMoney 
        最后再比较 maxMoney = max(taken, nonTaken)
        '''
        
        '''
        taken = 0
        nonTaken = 0
        maxMoney = 0
        for i in range(len(nums)):
            taken = nums[i] + nonTaken
            nonTaken = maxMoney
            maxMoney = max(taken, nonTaken)
        return maxMoney
        '''
        