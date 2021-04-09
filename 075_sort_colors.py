class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 以下方法是quicksort 用来排序的，适用于只有[0, 2]的情况，但此题还有个1
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right:
#             while left <= right and nums[left] < 1:
#                 left += 1
                
#             while left <= right and nums[right] > 1:
#                 right -= 1
                
#             if left <= right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1

        '''
        此题用三个指针，left, right 和index.
        index是一直跑的数字，left和right都是anchor. 等待被交换的数字。
        如果当前数字是0，那就和left anchor交换，同时向左走一步
        如果当前数字是2，那和right交换，right换过之后和left一样，都走一步
        但此时的anchor不一定要变，因为和right换来的数字可能还是2
        比如 2 0 1 2, index和right都是2，right可以向左走一步变成1
        但要保证index是0 or 1 所以要再和right换一次，变成1022
        
        如果当前数字是1，index自己走就好。anchor不变
        '''
        left, index, right = 0, 0, len(nums) - 1
        
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1
                
        