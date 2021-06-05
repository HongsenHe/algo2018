class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(res, candidates, target, [], 0)
        return res
    
    def helper(self, res, candidates, target, each, start):
        if target < 0:
            return
        
        if target == 0:
            res.append(list(each))
            return
        
        '''
        不能再回头，比如[2, 2, 3] 就不能再算[3, 2, 2]
        也就是需要start pointer, 来推动for loop.
        不同的是，此题需要target减去当前数字，而不是累加each对比target
        '''
        for i in range(start, len(candidates)):
            each.append(candidates[i])
            self.helper(res, candidates, target - candidates[i], each, i)
            each.pop()