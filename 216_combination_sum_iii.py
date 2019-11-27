class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.helper(res, [], k, n, 1)
        return res
    
    def helper(self, res, each, k, n, start):
        if n < 0:
            return
        
        if n == 0 and len(each) == k:
            res.append(list(each))
            return
        
        for i in range(start, 10):
            each.append(i)
            self.helper(res, each, k, n-i, i+1)
            each.pop()