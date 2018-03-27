class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        '''
        case 1 is k>0 and current num1 + k = num2 and num2 in nums list
        case 2 is k=0 and current num1 + 0 = num1 and num1 appears more than once
        case 3 is k>0 and current num1 - k = num2, but as looping nums, so num1 will be num2 later!
        k can not less than 0
        '''
        
        if k < 0:
            return 0
        
        ct = collections.Counter(nums)
        res = 0
        for num in ct:
            if k > 0 and num + k in ct or k == 0 and ct[num] > 1:
                res += 1
        return res