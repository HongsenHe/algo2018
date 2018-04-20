class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1, 3, 4, 1, 3]
        hm = {}
        
        for num in nums:
            if num in hm:
                hm.pop(num)
            else:
                hm[num] = 1
        return hm.keys()[0]
