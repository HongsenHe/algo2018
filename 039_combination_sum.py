class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper([], res, target, candidates, 0)
        return res
    
    def helper(self, each, res, target, candidates, start):
        if target < 0:
            return 
        
        if target == 0:
            res.append(list(each))
            return
        
        for i in range(start, len(candidates)):
            each.append(candidates[i])
            self.helper(each, res, target-candidates[i], candidates, i)
            each.pop()
        