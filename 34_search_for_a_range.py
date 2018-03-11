class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        res = []
        
        if not nums:
            return [-1, -1]
        
        while left + 1 < right:
            mid = left + (right-left) / 2
            if nums[mid] == target:
                # narrow down by moving right pointer to left side
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
                
        # find start index
        if nums[left] == target:
            res.append(left)
        elif nums[right] == target:
            res.append(right)
        else:
            return [-1, -1]
        
        # reset to find end index
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right-left) / 2
            if nums[mid] == target:
                # narrow down by moving left pointer to right side
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
            
        if nums[right] == target:
            res.append(right)
        elif nums[left] == target:
            res.append(left)
        else:
            return [-1, -1]
        
        return res        