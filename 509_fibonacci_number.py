class Solution:
    def fib(self, N: int) -> int:
        visited = {}
        return self.helper(visited, N)
    
    def helper(self, visited, N):
        if N < 2:
            return N
        if N in visited:
            return visited[N]

        res = self.helper(visited, N-1) + self.helper(visited, N-2)
        visited[N] = res
        
        return res
        