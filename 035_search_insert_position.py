class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] > target:
                # should skip mid no need compare, then use left <= right
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left
                


        