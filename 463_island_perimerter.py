class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        '''
        求小岛周长可以看每个点是不是小岛的一部分，如果是周长就加4，但如果有重复
        就要减去重复的边长2， 左上开始走起，相邻的是右边[i][j+1] 和下面[i+1][j]
        '''
        
        res = 0
        if not grid:
            return res
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i < m-1 and grid[i+1][j] == 1:
                        res -= 2
                    if j < n-1 and grid[i][j+1] == 1:
                        res -= 2
        return res
                 