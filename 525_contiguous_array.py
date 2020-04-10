class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 可以看成设置一个dummy node在数组开始，这样[0, 1]长度 为2 因为1 - (-1)
        hm = {0 : -1}
        pre_sum = 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                pre_sum -= 1
            else:
                pre_sum += 1
            
            # 还是积累子数组，如果当前积累在hm里找到，中间的差值就是答案之一
            if pre_sum in hm:
                res = max(res, i - hm[pre_sum])
            else:
                hm[pre_sum] = i
        return res
        