class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        maxFreq = 0
        res = 0
        
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        for k, v in dic.items():
            if v >= maxFreq:
                maxFreq = v
                res = k
        return res

    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for k, v in dic.items():
            if v > len(nums)//2:
                return k
        return None