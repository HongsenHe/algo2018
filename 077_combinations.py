class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(res, k, n+1, [], 1)
        return res
        
    def helper(self, res, k, n, each, start):
        if len(each) == k:
            res.append(list(each))
            return
        
        for i in range(start, n):
            each.append(i)
            self.helper(res, k, n, each, i+1)
            each.pop()
        