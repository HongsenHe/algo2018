class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(res, nums, [], 0)
        return res
    
    def helper(self, res, nums, each, start):
        # 既然是subset,所以把所有解（树的所有节点）放到结果集中
        res.append(list(each))
        
        # 举例：以1为开始，逐渐加入2， 3，即 需要start 并且传下去。
        # 然后以2位开始，但要继续走下去，避免21和12重复。
        for i in range(start, len(nums)):
            each.append(nums[i])
            self.helper(res, nums, each, i + 1)
            each.pop()