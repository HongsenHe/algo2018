class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            target = -nums[i]
            a = i + 1
            b = len(nums) - 1
            
            # skip the duplicated number
            if i and nums[i] == nums[i-1]:
                continue
            
            while a < b:
                if nums[a] + nums[b] > target:
                    b -= 1
                elif nums[a] + nums[b] < target:
                    a += 1
                else:
                    res.append([nums[i], nums[a], nums[b]])

                    # already found one solution, keep search based on current target!
                    a += 1
                    b -= 1
                    # deduplicating with the previous one, a vs a-1, b vs b+1
                    while a < b and nums[a] == nums[a-1]:
                        a += 1
                    while a < b and nums[b] == nums[b+1]:
                        b -= 1
                    
                    
            
        return res
                
            
        