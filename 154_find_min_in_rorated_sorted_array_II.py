class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        '''
        经典二分模板，此题一共有两种情况，345612 or 561234
        找到mid后和right比，如果mid < right的值，则可以压缩right部分
        即 right = mid，属于第二种情况。
        如果mid > right, 则是第一种情况，压缩left
        如果刚好相等，发现重复元素可以压缩right, 让right先进一步。
        
        最后找到了边界，返回两个指针的最小值。
        '''
        
        while left + 1 < right:
            mid = (left + right) // 2 
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right -= 1
        
        return min(nums[left], nums[right])