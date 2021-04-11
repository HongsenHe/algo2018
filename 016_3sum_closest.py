class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        min_diff = float('inf')
        nums.sort()
        
        index = 0
        
        '''
        看能否排序，能！那继续相向双指针，设一个固定点，降维成2sum问题。
        这样三个点可以凑成一个cur_sum, 看与target的差异即
        diff = abs(target -  cur_sum) 如果比最小的小，则更新。
        但答案是cur_sum 并不是diff. 
        双指针策略就是移动，如果cur_sum比target小，就移动left 
        使cur_sum大一些。同理移动 right
        
        '''
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[i]
                diff = abs(target -  cur_sum)
                
                if diff < min_diff:
                    min_diff = diff
                    res = cur_sum
                
                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return res