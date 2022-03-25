from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (1, -1), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
        
        '''
        经典BFS搜索题。
        需要什么？一个queue并且把初始点(0, 0)放入。一个visited set() 放入(0, 0)
        一个while queue， 一个is_valid func() 别越界且满足条件
        一个方向键dirs 且for loop dirs， 一个判断/退出条件。一个distance来维持答案
        
        过程：好比level order 需要把当前queue里的元素都pop出来，并且计算每个元素的8个方向
        
        '''
        queue = deque([(0, 0)])
        visited = {(0, 0), }
        distance = 1
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        
        # special case, has the solution
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        while queue:
            queue_size = len(queue)
            
            for _ in range(queue_size):
                orig_x, orig_y = queue.popleft()
                
                # 每次弹出来的node 是否符合条件
                if (orig_x, orig_y) == (max_row, max_col):
                    return distance
        
                # search neighbors
                for dir_x, dir_y in dirs:
                    cur_x = orig_x + dir_x
                    cur_y = orig_y + dir_y

                    if (cur_x, cur_y) in visited:
                        continue

                    if not self.is_valid(grid, cur_x, cur_y):
                        continue

                    queue.append((cur_x, cur_y))
                    visited.add((cur_x, cur_y))
                
            distance += 1
                    
        return -1
    
    def is_valid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0