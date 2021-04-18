class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        '''
        经典二分模板，之后要注意判断有几种情况。
        target在left的左边，就用左指针，
        target在left和right之间，就用右指针。
        不然就插入最后一个位置，即len(nums)
        '''
        
        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return len(nums)