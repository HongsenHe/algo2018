class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # left 不能和right 重合，要找到peak
        while left < right:
            mid = left + (right - left) // 2
            # 增长方向，挪移左指针
            if nums[mid] < nums[mid + 1]:
                # 可以越过mid, 因为mid+1 更大，可能是答案
                left = mid + 1
            else:
                # 不可越过mid, 因为mid > mid+1, mid可能是答案
                right = mid
                
        return left
        