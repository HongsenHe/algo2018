class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums)
        return nums
    
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        self.merge_sort(left)
        self.merge_sort(right)
        
        i = j = k = 0
        
        # here, same as merge two lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1
        
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1
            
            
        