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