class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        '''
        经典二分搜索题，分几种情况：
        如果中间点和左右都不相等，中间点是唯一，是答案！
        如果中间点index是奇数，要看它和前一个点是否相等，如果是则左半部分都合法，移动left pointer
        比如: [1, 1, 2, 3, 3, 4, 4], 中间点是 3和前一个点 2 不相等，就移动 right pointer
        
        或者中间点index是偶数，也是比较前一个点的情况
        比如: [1, 2, 2, 3, 3], 中间点2和前一个点 2 相等，移动right pointer到中间点
        
        只有一个点出现一次，其他都是两次意味着理想状况，偶数点是 第一次，奇数点是第二次。
        除非唯一点打破了顺序。
        最后left < right 跳出循环，也是经典套路，看看left, right都在哪里，有就返回。
        '''
        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            
            if mid % 2 == 1:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] == nums[mid-1]:
                    right = mid
                else:
                    left = mid
                        
        if nums[left]:
            return nums[left]
        else:
            return nums[right]