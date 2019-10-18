class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lng = len(nums)
        # 从后往前找，找到一个上升点的尾巴则退出 [1,2,3,5,4] 3<5
        for i in range(lng-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            # 如果是一个纯降序的数列，则翻转是答案 
            # 比如：[3,2,1] 一路下降，翻转成[1,2,3]
            nums.reverse()
            return nums
        
        # 把后面降序的都翻转了，变成[1,2,3,4,5]
        for j in range(lng-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        # 比较复杂。。。
        for j in range(0, (lng - i)//2):
            nums[i+j+1], nums[lng-j-1] = nums[lng-j-1], nums[i+j+1]
        return nums        