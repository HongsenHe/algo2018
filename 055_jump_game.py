class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        
        '''
        贪心算法，从后往前走，
        如果当前的idx和当前的num可以达到或者超越 终点（last_pos)
        那么把这个终点挪到当前的idx. 
        for loop是从后到前，不断的选择可以达到终点的idx 并且更新终点
        直到终点就是启动 即 last_pos == 0 也就找到了答案。
        '''
        
        for i in range(last_pos, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
                
        return last_pos == 0
            
