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
        
        money[i] 表示到了第i个房子，能偷多少？第i个房子，但nums index其实是i-1
        好比到了第3个房子，你能偷多少money[3], 但是在nums里面，index = 2 
        即，i-1, 当前房子能偷nums[i-1]
        money[i] = max(nums[i-1] + money[i-2], money[i-1])
        没有房子的时候，设置为0， 最后就看有n个房子的时候能偷多少，也就是money[n],
        '''
        
        
        # Space O(n)
        n = len(nums)        
        if not nums:
            return 0
        if n < 3:
            return max(nums)
        
        money = [0] * (n+1)
        money[0] = 0
        money[1] = nums[0]
        for i in range(2, n+1):
            # i 要从2开始，money[2] 代表偷第2个房子的时候的情况
            # 所以这里要用i-1 也就是 nums[1] 也就是用第二个房子的价值
            money[i] = max(nums[i-1] + money[i-2], money[i-1])
        return money[n]
        
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
        