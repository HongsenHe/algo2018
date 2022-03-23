from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        '''
        03232022 
        BFS 版本，先找到所有边界上值为O的节点，放到queue中作为初始节点。
        套用模板，把所有和这些边界节点相连的（符合条件的）都标记 visited
        并且放到queue里继续滚动。
        
        最后再撸一遍board， 所有已经在visited里的可以不变，因为和边界O相连
        其他都变成X
        
        '''
        
        m = len(board)
        n = len(board[0])
        
        queue = deque()
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        # 寻找所有在边界的并且是O的坐标，放入queue里，作为第一批节点
        for i in range(m):
            for j in range(n):
                # 当前不是X，略
                if board[i][j] == 'X':
                    continue
                    
                # 不在边界，略
                if not (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    continue
                    
                queue.append((i, j))
                visited.add((i, j))
                
        # BFS模板，开始以边界且为O的一批节点作为初始节点，凡是相邻且O的，标记成A
        while queue:
            orig_x, orig_y = queue.popleft()
            
            for dir_x, dir_y in dirs:
                cur_x = orig_x + dir_x
                cur_y = orig_y + dir_y
                
                if not self.is_valid(cur_x, cur_y, board):
                    continue
                    
                if (cur_x, cur_y) in visited:
                    continue
                    
                queue.apppend((cur_x, cur_y))
                visited.add((cur_x, cur_y))
                
        # 把所有还没访问过的节点，都变成X
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if (i, j) not in visited:
                    board[i][j] = 'X'
                    
    def is_valid(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O'
        
        
        # DFS 版本
        
#         if not board:
#             return board
        
#         '''
#         切入点：
#         例子中，最后一行的O不能变成X，如果他上面的也是O，则都不能变成X。
#         所以要看四条边界的数字，用DFS来遍历，如果是O就变成一个特殊的字符A
#         这样就是寻找和边界相连的O，都变成A
#         最后再循环一次，把其余的O都变成X，把A还原成O
#         '''
#         m = len(board)
#         n = len(board[0])
        
#         for i in range(m):
#             for j in range(n):
#                 if i in [0, m-1] or j in [0, n-1] and board[i][j] == 'O':
#                     self.helper(i, j, board)
                    
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'O':
#                     board[i][j] = 'X'
#                 elif board[i][j] == 'A':
#                     board[i][j] = 'O'
    
#     def helper(self, i, j, board):
#         if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
#             return
        
#         board[i][j] = 'A'
#         self.helper(i+1, j, board)
#         self.helper(i-1, j, board)
#         self.helper(i, j+1, board)
#         self.helper(i, j-1, board)
                
                
        
        
        
        
        
        
        
        
        
        
        
                