class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        如何找到某些数字没在序列里？比如5，6不在[4,3,2,7,8,2,3,1]里面
        可以看index=5，6的数字情况。也就是变动非index=5，6 正数变负数
        再遍历一下数列，如果当前的没有被动过，就是index=5，6 即是结果。
        '''
        
        nums = [0] + nums
        for num in nums:
            index = abs(num)
            # 改变非5, 6的数字，变为负数，即使重复也没事
            nums[index] = -abs(nums[index])
        return [i for i in range(len(nums)) if nums[i] > 0]

    # 04182019
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        nums2 = set(nums)
        for i in range(1, len(nums)+1, 1):
            if i not in nums2:
                res.append(i)
        return res