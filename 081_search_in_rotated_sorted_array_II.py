class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        '''
        04152021
        如果数组里有重复数字，不一定用binary search
        比如[1, 1, ..0... 1] 很多个1，只有一个0，找0
        则要去重很多或者无法分一半，则退化成O(n) 
        所以可以直接用暴力解法
        '''
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False



        # binary search, worse case O(n)
        left, right = 0, len(nums) - 1
         
        while left +  1 < right:
            mid = (left + right) // 2
            
            # skip duplicated num
            while left < mid and nums[left] == nums[mid]:
                left += 1
            
            if nums[mid] == target:
                return True
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
                    
        if nums[left] == target or nums[right] == target:
            return True
        
        return False
            
            
                