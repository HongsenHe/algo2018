class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        dfs/回溯/memo 问题。设一个pos不断前进把当前数字加入cur_sum中。
        每一层有两种情况：-/+, 因此和是两个helper的总和。
        
        为了避免重复计算，可以设visited来保存当前层和结果。如果找到则使用。
        '''
        def helper(pos, cur_sum):
            key = (pos, cur_sum)
            
            if key not in visited:
                if pos == len(nums):
                    return 1 if cur_sum == target else 0
                else:
                    visited[key] = helper(pos + 1, cur_sum + nums[pos]) + helper(pos + 1, cur_sum - nums[pos])

            return visited[key]
        
        visited = {}
        return helper(0, 0)
        
