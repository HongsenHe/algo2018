class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local = float('-inf')
        res = float('-inf')
        
        for num in nums:
            # if previous (sum of 0 to i-1) < 0, then use current otherwise add on!
            local = max(num, num + local)
            # as current num could be < 0, after add on, this could be < global max
            res = max(local, res)
        return res

    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = 0
        
        for num in nums:
            cur_max += num
            if cur_max > res:
                res = cur_max
        # 如果当前元素让合集是负数，不如舍弃，归零。
        if cur_max < 0:
                cur_max = 0
        return res

    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = nums[0]
        for num in nums[1:]:
            # if previous cur_max < 0, count from current num
            if cur < 0:
                cur = num
            else:
                cur += num
            res = max(res, cur)
        return res