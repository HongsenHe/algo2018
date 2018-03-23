class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for x in range(0, len(nums) - 2):
            # skip duplicated number, as calculated
            if x and nums[x] == nums[x - 1]:
                continue
            
            target = -nums[x]
            i = x + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[x], nums[i], nums[j]])
                    j -= 1
                    i += 1
                    # deduplicating
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    i += 1
        return res
  