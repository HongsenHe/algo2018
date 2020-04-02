class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        diff_min = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            a = i + 1
            b = len(nums) - 1
            
            while a < b:
                cur_sum = nums[i] + nums[a] + nums[b]
                diff = abs(cur_sum - target)
                if diff < diff_min:
                    diff_min = diff
                    res = cur_sum
        
                if diff == 0:
                    return target
                elif cur_sum < target:
                    a += 1
                elif cur_sum > target:
                    b -= 1
        return res
                
            