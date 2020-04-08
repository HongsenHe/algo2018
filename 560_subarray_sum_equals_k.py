class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        dic = {0:1}
        # find nums[i] - nums[j] = k like 2sum question
        
        for num in nums:
            total += num
            if total - k in dic:
                res += dic[total-k]
            if total not in dic:
                dic[total] = 1
            else:
                dic[total] += 1
        return res
                
        