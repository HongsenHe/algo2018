class Solution:
    # it works, but TLE
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         res = []
#         self.helper(res, [], nums, target)
#         return len(res)
    
#     def helper(self, res, each, nums, target):
#         if target < 0:
#             return
#         if target == 0:
#             res.append(list(each))
#             return
        
#         for i in range(len(nums)):
#             each.append(nums[i])
#             self.helper(res, each, nums, target-nums[i])
#             each.pop()
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target+1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i-n]
        return dp[-1]