class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            return -1
        in_degree = [0] * (N+1)
        out_degree = [0] * (N+1)
        for tr in trust:
            out_degree[tr[0]] += 1
            in_degree[tr[1]] += 1
            
        '''
        图论
        分为in_degree 入度和out_degree出度，构建邻接表
        对于符合者，其他所有人N-1 指向他, 也就是in_degree[i] == N-1
        同时他不能指向其他节点，所以out_degree[i] == 0
        
        '''
        for i in range(1, N+1, 1):
            if in_degree[i] == N-1 and out_degree[i] == 0:
                return i
        return -1
