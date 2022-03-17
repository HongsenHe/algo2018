class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
#         '''
#         sliding window的方法，求k区间的和，可以用 nums[i] - nums[i - k]
#         求差值来获得，这样就把原来的改了。好处是不必每次都求 nums[i : i + k]
        
#         此题是643的变种，k'有范围, 即从k 到 n，可以用列举每个符合条件的k
#         或者 二分法来解决。
        
#         '''
#         res = float('-inf')
#         n = len(nums)
        
#         for i in range(k, n + 1):
#             res = max(res, self.cal(nums, i))
            
#         return res
        
#     def cal(self, nums, k):
#         res = cur = sum(nums[:k])
#         for i in range(k,len(nums)):
#             cur += nums[i] - nums[i-k]
#             res = max(res, cur)

#         return res / k
    
    
        # from jiuzhang
        if not nums:
            return 0
            
        start, end = min(nums), max(nums)
        while end - start > 1e-5:
            mid = (start + end) / 2
            if self.check_subarray(nums, k, mid):
                start = mid
            else:
                end = mid
                
        return start
        
    def check_subarray(self, nums, k, average):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)
            
        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])
            
        return False