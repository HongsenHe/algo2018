class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hm = {0: -1}
        pre_sum = 0
        
        for i in range(len(nums)):
            pre_sum += nums[i]
            
            if k != 0:
                pre_sum = pre_sum % k
                
            if pre_sum in hm and i - hm[pre_sum] > 1:
                return True
            
            if pre_sum not in hm:
                hm[pre_sum] = i
            
        return False
                
        
        '''
        [23, 2, 22, 2, 6, 7]
        23 % 6 = 5: 0
        25 % 6 = 1: 1
        47 % 6 = 5: 2 (在hm里，而且index 0和2的距离大于1，找到答案)
            23和47的关系，刚好差了N个6，即每次把pre_sum % 6的结果放到hm里
            如果两个pre_sum 中间有一组数字凑成6N，即是答案。
        49 % 6 = 1: 3 (即22和2也组成了6N, 
            用当前的坐标3减去hm里的坐标1即另一组答案, nums[1:3]，本题不要求)
            
        pre_sum的思想是不断累加，做一些操作放到hm里。并且记录index.
        直到下一个pre_sum在hm发现已存在，即使答案。
        
        '''