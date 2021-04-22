from collections import deque
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        04222021 可以套用经典BFS模板
        对于每一个点，如果本身是岛并且之前没访问过就进行BFS判断其邻居。
        邻居可以用DIRECTIONS表示
        如果邻居都是岛，那就是连通块，即以当前点开始的一个岛。
        '''

        if not grid or not grid[0]:
            return 0
        
        visited = set()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(i, j, grid, visited)
                    res += 1
                    
        return res

    def bfs(self, x, y, grid, visited):
        '''
        套用BFS模板，先把当前坐标以tuple的方式加进去 (x, y)
        并且马上加入visited集合。
        模板总是以while queue开始，先弹出来一个坐标。
        并且对其邻居展开调查。或者图的node.get_neighbors()
        对于每一个邻居用同样方法判断，可以包装is_valid 函数
        如果符合要求，则把邻居加入queue 等待下一层处理
        并且马上加入visited 集合。
        '''
        queue = deque([(x, y)])
        visited.add((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y
                
                if not self.is_valid(new_x, new_y, grid, visited):
                    continue
                    
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
    
    def is_valid(self, x, y, grid, visited):
        m = len(grid)
        n = len(grid[0])
        
        '''
        每题不一样，但都要判断当前坐标x, y是否出界了。
        也要判断是否符合要求，即 grid[x][y] 是否是0 or 1
        最后要判断是否 访问过，标准操作。
        '''
        if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or grid[x][y] == '0':
            return False
            
        return True
        
                    
            
# DFS
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
                    
                