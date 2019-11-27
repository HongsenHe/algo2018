class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.helper(res, [], candidates, target, 0)
        return res
    
    def helper(self, res, each, candidates, target, start):
        if target < 0:
            return
        if target == 0:
            if each not in res:
                res.append(list(each))
            return
        
        for i in range(start, len(candidates)):
            each.append(candidates[i])
            self.helper(res, each, candidates, target-candidates[i], i+1)
            each.pop()