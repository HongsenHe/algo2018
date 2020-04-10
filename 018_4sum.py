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