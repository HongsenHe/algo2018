class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0, 0)
        
        
    def helper(self, board, i, j):
        '''
        首先有三种特殊情况
        如果当前行i到达了最后，那就是完成了所有搜索，返回True
        如果当前列j到达了最后，就搜索下一行即，i+1
        如果当前数字是已知的，就跳过去搜索下一列即, j+1, 直到此行结束
        '''
        if i == 9:
            return True
        if j >= 9:
            return self.helper(board, i + 1, 0)
        
        if board[i][j] != '.':
            return self.helper(board, i, j + 1)
        
        # 要填充的数字是从1 - 9， str type
        for c in range(1, 10, 1):
            val = str(c)
            # 如果当前位置i, j 不能填充当前的数字，就继续吧            
            if not self.is_valid(board, i, j, val):
                continue
            
            '''
            经典回溯套路：
            1. 如果当前位置i, j 可以填充当前数字val, 就改变当前数字
            2. 继续搜索，也就是调用helper函数并且下一列
            3. 还原当前位置成为'.'
            '''
            
            board[i][j] = val
            if self.helper(board, i, j + 1):
                return True
            board[i][j] = '.'
    
        return False
        
        
    def is_valid(self, board, i, j, val):
        '''
        判断当前的位置i j 和当前要填充的数字val 是否合法。
        1. 判断当前位置的那一列，也就是对于col = j, row from 0 to 9, 如果有和要填充的val相等就是非法
        2. 同理判断当前位置的那一行，也就是对于row = i, col from 0 to 9
        3. 判断9个小方块， 要填充的val是唯一数字
        4. 不必判断填充的数字和全局解比较，也比不了。如果都满足就合法，如果后来不符合全局，也可以回溯回来。
        '''
        for row in range(9):
            if board[row][j] == val:
                return False
        for col in range(9):
            if board[i][col] == val:
                return False
        row = i - i % 3
        col = j - j % 3
        for x in range(3):
            for y in range(3):
                if board[x + row][y + col] == val:
                    return False
        return True