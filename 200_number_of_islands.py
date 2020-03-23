class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        DFS、BFS。只要遍历一遍，碰到一个1，就把它周围所有相连的1都标记为非1，
        这样整个遍历过程中碰到的1的个数就是所求解。
        时间 O(NM) 空间 O(max(N,M)) 递归栈空间
        """
        count = 0        
        if not grid:
            return 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果找到1，即找到一个岛，
                if grid[i][j] == '1':
                    count += 1
                    # 并且把岛周围都变成海水，即set to 0
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid, i, j):
        # 套路： 1. 边界条件
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        
        # 2. do something, 即变成海水
        grid[i][j] = '0'
        
        # 3. 在此基础上，继续搜索
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
                    
                