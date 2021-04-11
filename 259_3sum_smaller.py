class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return 0
        
        nums.sort()
        res = 0
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[i]
                
                if cur_sum < target:
                    '''
                    比较tricky的地方是，要把left和right之间的数字都加进去
                    比如-5, -4, -3, -2, 5 target = 7
                    当找到-5, -4 (left), 5 (right)的时候，其中
                    (-3, 5), (-2, 5) 也都符合
                    一共有right - left = 4 - 1 = 3 都符合。
                    
                    如果sub_sum > target了，需要移动left += 1
                    反正缩小right
                    '''
                    res += right - left
                    left += 1
                else:
                    right -= 1

        return res