class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        100th question so far!
        创建一个helper函数，找到数组中的最大值，但还是有个天花板，即上一个最大值。
        比如找第一最大值，天花板就是正无穷，第二最大值的天花板就是第一最大值，你懂的！
        '''
        
        max1 = self.helper(float('inf'), nums)
        max2 = self.helper(max1, nums)
        max3 = self.helper(max2, nums)
        if max3 == float('-inf'):
            return max1
        return max3
    
    def helper(self, maxNum, nums):
        curMax = float('-inf')
        for num in nums:
            if num > curMax and num < maxNum:
                curMax = num
        return curMax
            
        