class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, '', 0, 0, n)
        
        '''
        04202022
        n个pairs 则最终长度是2*n, 即递归跳出条件。
        合法的括号必须是一对 () 那就要先放( , 一直到 left < n
        再放), 直到 right < left (虽然最后也是right < n)
        '''
        

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

    # 06162021 一样的方法，更直观的Backtracking...
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, n, [], 0, 0)
        
        return res
    
    def helper(self, res, n, each, left, right):
        if len(each) == 2 * n:
            res.append("".join(each))
            return
            
        if left < n:
            each.append('(')
            self.helper(res, n, each, left + 1, right)
            each.pop()
            
        if right < left:
            each.append(')')
            self.helper(res, n, each, left, right + 1)
            each.pop()
            