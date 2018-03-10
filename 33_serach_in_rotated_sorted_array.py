class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        the key point is the make sure where is the mid pts. 
        so compare left with mid value
        make sure it's continuous rising, then use binary search.
        """
        
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            
            # this is continuous rising part
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # this is called 'broken' part
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                        
                
                