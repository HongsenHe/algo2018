class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
#         res = float('-inf')
        
#         for i in range(len(nums) - k + 1):
#             res = max(res, sum(nums[i: i + k]) / k)
            
#         return res
            
        '''        
        sliding window的方法，求k区间的和，可以用 nums[i] - nums[i - k]
        求差值来获得，这样就把原来的改了。好处是不必每次都求 nums[i : i + k]
        '''
        res = now = sum(nums[:k])
        for i in range(k,len(nums)):
            now += nums[i] - nums[i-k]
            res = max(now, res)
            
        return res/k