class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        能排序先排序，然后双指针。
        对于每一个数，作为target. 看这个数之前的array 是否能满足条件
        比如当前 index = i, 就看 0到 i-1之间是否能找到两边之和大于nums[i]
        
        如果可以就成批的把答案写入，一共个数是 right - left
        同时继续找，要把右指针向左移动，让这两个边小一些看看是否满足。
        如果这两边小于当前的数（最大边）移动left += 1
        
        '''
        nums.sort()
        res = 0
        
        for i in range(len(nums)):
            left, right = 0, i - 1
            
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
                    
        return res
            