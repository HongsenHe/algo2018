class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        看有多少个数字n 也就是nums的长度，求和n*(n-1)/2 = 6
        遍历数组，减去每一项 最后就是缺的数字
        '''
#         n = len(nums) + 1
#         target = n * (n-1) // 2
#         for num in nums:
#             target -= num
#         return target
    
        # pythonic
        return len(nums)*(len(nums)+1)//2 - sum(nums)
