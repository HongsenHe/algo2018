class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        return [self.binary_search_first(nums, target), self.binary_search_last(nums, target)]

    def binary_search_first(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # 要找first position 所以严格小于target才移动start
            # [1, 2, 2, 2, 2, 2, 3] 希望尽量移动end指针缩小范围
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    
    def binary_search_last(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # 要找last position 如果等于也移动start 指针，
            # [1, 2, 2, 2, 2, 2, 3] 压缩到右边
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
    