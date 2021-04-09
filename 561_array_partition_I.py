class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''
        遇到 array 问题看是否可以sort. 如果可以就先sort 用双指针或者BS来思考。
        排序之后变成， 1, 2, 3, 4 也就是 min(1, 2) + min(3, 4)
        也就是只找偶数Index的数字 sum就好。
        '''
        
        if not nums:
            return 0
        
        nums.sort()
        res = 0
        
        for i in range(0, len(nums), 2):
            res += nums[i]
            
        return res
            
        