class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        def helper(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + helper(i-1, j) + helper(i+1, j) + helper(i, j-1) + helper(i, j+1)
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = helper(i, j)
                    res = max(res, area)
        return res
    
    