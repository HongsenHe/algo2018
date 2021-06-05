class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(n, k, res, [], 1)
        return res
    
    def helper(self, n, k, res, each, start):
        # 退出条件是 当前子集长度满足条件
        if len(each) == k:
            res.append(list(each))
            return
        
        # 可以横向（每一层）算是一个for loop 对于当前层，拿出1放进子集
        # 再进入下一层，要从2开始，即需要start point
        # 不断回溯，凑成12， 13， 14， 然后再以2开始的子集
        for i in range(start, n + 1):
            each.append(i)
            self.helper(n, k, res, each, i + 1)
            each.pop()
