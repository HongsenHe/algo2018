class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lng = len(nums)
        # 从后往前找，找到一个上升点的尾巴则退出 [1,5,8,4,7,6,5,3,1] 4<7
        for i in range(lng-2, -1, -1):
            if nums[i] < nums[i+1]:
                # i = 3, num = 4
                break
        else:
            # 如果是一个纯降序的数列，则翻转是答案 
            # 比如：[3,2,1] 一路下降，翻转成[1,2,3]
            nums.reverse()
            return nums
        
        # 在后面降序里找到第一个比转折点大的数字，交换
        # 1,5,8,4是前部分，4是转折点，7,6,5,3,1是降序，变成[1,5,8,5,7,6,4,3,1]
        for j in range(lng-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        # 翻转降序部分，从[1,5,8,5,7,6,4,3,1] -> [1,5,8,5,1,3,4,6,7]
        for j in range(0, (lng - i)//2):
            nums[i+j+1], nums[lng-j-1] = nums[lng-j-1], nums[i+j+1]
        return nums        