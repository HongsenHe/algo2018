class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        
        '''
        切入点：
        例子中，最后一行的O不能变成X，如果他上面的也是O，则都不能变成X。
        所以要看四条边界的数字，用DFS来遍历，如果是O就变成一个特殊的字符A
        这样就是寻找和边界相连的O，都变成A
        最后再循环一次，把其余的O都变成X，把A还原成O
        '''
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if i in [0, m-1] or j in [0, n-1] and board[i][j] == 'O':
                    self.helper(i, j, board)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
    
    def helper(self, i, j, board):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return
        
        board[i][j] = 'A'
        self.helper(i+1, j, board)
        self.helper(i-1, j, board)
        self.helper(i, j+1, board)
        self.helper(i, j-1, board)
                
                