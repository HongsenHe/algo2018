class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, res, [])
        
        return res
    
    def helper(self, nums, res, cur):
        if len(cur) == len(nums):
            res.append(list(cur))
            return
        
        for i in range(len(nums)):
            # duplicated, skip
            if nums[i] in cur:
                continue
            cur.append(nums[i])
            self.helper(nums, res, cur)
            cur.pop(-1)
        