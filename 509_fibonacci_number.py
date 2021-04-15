class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        '''
        如果纯递归 time = O(2^n) 需要使用记忆化搜索
        '''
        visited = {0: 0, 1: 1}
        return self.helper(visited, n)
        
    def helper(self, visited, n):
        if n in visited:
            return visited[n]
        
        res = self.helper(visited, n - 1) + self.helper(visited, n - 2)
        visited[n] = res
        
        return res

        '''
        or return self.helper(visited, n) 不需要res
        '''
