class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        把数组不大于n的正整数放到下标+1 与其 数值相同的位置上，第一个 下标+1 !=数值的就是返回值
        nums = [3, 4, -1, 1] 变化成 [1, -1, 3, 4] 1就是index 0 + 1
        3 是 index 2 + 1, 但-1却不满足 所以返回2
        
        举例: [7,8,9,11,12] 排序之后还是这个，但第一个missing positive不是10，而是6
        也就是返回index = 1
        两个for loop, 第一个构建，第二个查找, Time = O(n), Space = O(1)
        
        '''
        n = len(nums)
        for i in range(n):
            '''
            要特别理解这段核心代码
            num[i] > 0: 要保证正数
            nums[i] <= n: 如果超过nums本身长度了不需要考虑，因为missing num在之前发生
            nums[i] != i + 1: 如果满足条件 i + 1 == nums[i], skip
            nums[i] != nums[nums[i] - 1]: 如果这个i位置的数字不符合条件，要把这个i位置本来的数字换过来
                比如 [1, 5, 3, 4, 6] i = 1的时候，要把2调过来，同时把5送去index = 4的位置
                也就是5和6互换。直到满足所有条件，跳出while, 继续计算i = 2
            '''
            while nums[i] > 0 and nums[i] <= n and \
              nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        
        return n + 1
    
    
        #         if not nums:
    #             return 1
    #         max_num = max(0, max(nums))
    #         for i in range(1, max_num):
    #             if i not in nums:
    #                 return i
    #         return max_num + 1