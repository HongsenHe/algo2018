class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n):
            target = -nums[i]
            left = i + 1
            right = n - 1
            
            # cur = prev, 已经计算过，skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while left < right:
                cur_sum = nums[left] + nums[right]
                
                if cur_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # 向回看，cur = prev, skip
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return res