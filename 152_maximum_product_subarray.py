class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        '''
        Kadane's algo. similar with max subarray, but need maintain
        a cur_min, eg. cur_min = -10, and cur num = -2, then max will be 20
        res should always compare with cur_max and itself.
        '''
        
        for i in range(1, len(nums)):
            num = nums[i]
            tmp = cur_max
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(tmp * num, cur_min * num, num)
            res = max(res, cur_max)
        return res