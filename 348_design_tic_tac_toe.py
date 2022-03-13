class TicTacToe:
    '''
    03122022 
    暴力解法，对于最后一步棋，即当前的row, col, 分别判断它所在的row/col/diagonal
    注意 diagonal有两种，分别判断。

    '''

    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        
        if self.check_row(row, player) or self.check_col(col, player) or self.check_diagonal_1(player) or self.check_diagonal_2(player):
            return player
        
        return 0
        
    def check_row(self, row, player):
        # check row
        win_row = self.board[row]
        for elem in win_row:
            if elem != player:
                return False
            
        return True
    
    def check_col(self, col, player):
        # check col
        for i in range(self.n):
            if self.board[i][col] != player:
                return False
                    
        return True
    
    def check_diagonal_1(self, player):
        # check diagonal
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    continue
                    
                if self.board[i][j] != player:
                    return False
        return True
    
    def check_diagonal_2(self, player):
        for i in range(self.n):
            for j in range(self.n - 1, -1, -1):
                if abs(i) + abs(j) != self.n - 1:
                    continue
                    
                if self.board[i][j] != player:
                    return False
                
        return True
                
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)