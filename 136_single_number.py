class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1, 3, 4, 1, 3]
        hm = {}
        
        for num in nums:
            if num in hm:
                hm.pop(num)
            else:
                hm[num] = 1
        return list(hm.keys())[0]


        O(1) memory
        res = 0
        '''
        XOR thing:
        a ^ a = 0
        a ^ 0 = a
        '''
        for num in nums:
            res ^= num
        return res
        
