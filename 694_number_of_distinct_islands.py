class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        所以公认的难点还是在于如何判断两个岛是平移的。。。就看坐标吧
        把每个点的坐标变成相对坐标，基准就是左上的那个点的坐标
        定义大岛由几个小岛组成：
        (x-i, y-j), x, y是当前小岛的坐标即grid[x][y] == 1, 
        i, j是当前大岛，左上的坐标，这样就能求每个小岛的相应坐标。
        如果求过了就不加进去了，保证没重叠点，如果没有要把当前小岛绝对坐标放到seen()里。
        然后再以当前(i,j)为起点，求四周。然后再放到大的集合里面，看有多少独特的岛！
        '''
        m = len(grid)
        n = len(grid[0])
        seen = set()

        def helper(x, y, i, j):
            if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in seen:
                seen.add((x, y))
                # 相对位置
                shape.add((x - i, y - j))
                helper(x+1, y, i, j)
                helper(x-1, y, i, j)
                helper(x, y+1, i, j)
                helper(x, y-1, i, j)
                
        shapes = set()
        for x in range(m):
            for y in range(n):
                shape = set()
                helper(x, y, x, y)
                if shape:
                    shapes.add(frozenset(shape))
        return len(shapes)
                    