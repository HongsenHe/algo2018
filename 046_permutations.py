class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        level = []
        
        if not nums:
            return res
        
        self.helper(nums, level, res)
        return res
        
        
    def helper(self, nums, level, res):
        if len(nums) == len(level):
            res.append(list(level))
            return
        
        for i in range(len(nums)):
            cur = nums[i]
            if cur in level:
                continue
            level.append(cur)
            self.helper(nums, level, res)
            level.pop()
            
        
        