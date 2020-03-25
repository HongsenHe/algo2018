class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return(self.search_left(nums, target), self.search_right(nums, target))
        
    
    def search_left(self, nums, target):
        idx = -1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # two cases: narrow down by moving the right pointer to the mid
            # and calculate left - mid side only
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
                
            # find find the value, unlike the traditional BS, don't return
            # keep this mid index, this part is doing left - mid, so if
            # this mid is the only one, then use it. if it's not the left most
            # just update it.
            if nums[mid] == target:
                idx = mid
                
        return idx
    
    
    def search_right(self, nums, target):
        idx = -1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
            if nums[mid] == target:
                # calculate mid - right side
                idx = mid
        return idx
        