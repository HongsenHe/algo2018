class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            num1 = nums[i]
            target1 = target - num1
            
            for j in range(i+1, n):
                num2 = nums[j]
                target2 = target1 - num2
                
                # same as 2 sum
                hm = set()
                for k in range(j+1, n):
                    if target2 - nums[k] in hm:
                        # list cannot be hashed, use tuple here for set()
                        res.append((num1, num2, target2 - nums[k], nums[k]))
                    else:
                        hm.add(nums[k])
        return set(res)



# two pointers
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        nums.sort()
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                target_2 = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    if left < right and nums[left] + nums[right] < target_2:
                        left += 1
                    elif left < right and nums[left] + nums[right] > target_2:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
        return res
                        
