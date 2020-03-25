class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # usually mid data <= right data in sorted list
            # if so, then the min data is in mid - right
            if nums[mid] > nums[right]:
                # +1, as mid is not the min data, mid is already greater than right
                # so use +1 for skipping the mid position
                left = mid + 1
            else:
                # mid could be equal to right, so do not skip mid
                # if mid < right, mid could be the min data, anyway do not skip mid
                right = mid
                
        return nums[left]
                