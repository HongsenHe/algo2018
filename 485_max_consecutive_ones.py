class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # j = -1
        # nums.append(0)
        # res = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         res = max(res, i-j-1)
        #         j = i
        # return res
        
        count = res = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        return max(res, count)
                