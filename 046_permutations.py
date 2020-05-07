class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, res, [])
        return res
    
    def helper(self, nums, res, cur):
        if len(cur) == len(nums):
            res.append(list(cur))
            return
        
        for num in nums:
            if num in cur:
                continue
            cur.append(num)
            self.helper(nums, res, cur)
            cur.pop()