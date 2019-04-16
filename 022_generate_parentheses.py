class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, '', 0, 0, n)
        return res
    
    def helper(self, res, sub, left, right, n):
        if len(sub) == 2*n:
            # 边界条件：子答案的长度等于总长度跳出
            res.append(sub)
            return 
        
        # 如果开括号还有，即插入当前结果，同时数量+1（消耗一个）
        if left < n:
            self.helper(res, sub+'(', left+1, right, n)
        # 如果闭括号数量小于开括号，可以插入当前结果， 同时数量+1（消耗一个）
        if right < left:
            self.helper(res, sub+')', left, right+1, n)