class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in hm:
                return [hm[num], i]
            else:
                hm[target-num] = i
        return false
    