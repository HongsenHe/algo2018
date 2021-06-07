class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.helper(res, [], 0, nums)
        return res
    
    def helper(self, res, each, start, nums):
        # 确保有唯一解，既然排序过，只需把每一个each放到结果集中
        if each not in res:
            res.append(list(each))
        
        for i in range(start, len(nums)):
            each.append(nums[i])
            self.helper(res, each, i+1, nums)
            each.pop()
            