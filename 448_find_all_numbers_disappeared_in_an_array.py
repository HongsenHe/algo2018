class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        获得遇到当前的数字的绝对值index 改变数组中index的数字变为负数
        比如4，就把nums[4]的数字改为负数，这样算是找到了'4'的位置
        循环一遍发现只有index 5和6的数字还是正数，说明没有5和6的idx, 就是答案！
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