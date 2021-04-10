class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         anchor = 0        
#         cur = 0
        
#         '''
#         模拟问题，用一个anchor 总是锚定0，等待running index和它互换。
#         一旦cur running index找到越过anchor并且不是0的数字，就交换。
#         然后两个指针前进一步。如果当前也是0，就自己走一步。比较麻烦但直观思考。
#         '''
#         while cur < len(nums):
#             while anchor < len(nums):
#                 if nums[anchor] == 0:
#                     break
#                 anchor += 1
                
#             if cur > anchor and nums[cur] != 0:
#                 nums[anchor], nums[cur] = nums[cur], nums[anchor]
#                 anchor += 1
#                 cur += 1
#             else:
#                 cur += 1
        
#         return nums
    
        '''
        同向双指针，anchor问题。思考一个anchor总是锚定0，等待被交换。
        如果当前数字不是0，则交换，代码：
        if nums[cur]:
            nums[cur], nums[anchor] = nums[anchor], nums[cur]
            
        理解这步之后要考虑交换之后要做什么？
        交换之后，anchor不再是0，需要前进一步，则 anchor += 1
        在for loop里，每次cur都会前进一步
        
        如果当前数字是0，则anchor不动，只让cur继续向前跑。
        所以for loop里 并没有else
        
        '''
        
        anchor = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[cur], nums[anchor] = nums[anchor], nums[cur]
                anchor += 1
        return nums
            