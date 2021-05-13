class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        对于当前数字，要找到其是否有前一个prev, 和下一个next.如果有继续找。
        但要从这个序列的最小值开始，只找next就好。
        即如果prev在nums里，则 跳过。
        找到最后打擂台，更新结果。
        
        '''
        
        if not nums:
            return 0
        
        max_length = float('-inf')
        nums_set = set(nums)
        
        for num in nums:
            prev = num - 1
            
            if prev not in nums_set:
                next = num + 1
                cur_length = 1
                
                while next in nums_set:
                    cur_length += 1
                    next += 1
                    
                max_length = max(max_length, cur_length)
                
        return max_length
                    
                
                
        