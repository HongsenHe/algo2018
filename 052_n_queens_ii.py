class Solution:
    def totalNQueens(self, n: int) -> int:
        # board 存储一种解法（作为缓存）
        self.board = [0 for _ in range(n)]
        # boards 存储所有解法（作为结果）
        self.res = 0

        '''
        总体思路就是回溯方法，只研究第一行的第一列到最后一列，
        依次放皇后，每次都判断是否冲突，如果能放，
        把皇后的列写入候选结果，如果不行，就折回继续查找。
        到最后一行，就根据规则打印结果，并且返回所有结果。
        '''
        self.solve_line(0, n)
        return self.res

    def solve_line(self, row, n):
        # 每一行只能放一个皇后，如果是最后一行，那就是已经放了N个皇后, 
        # 结果+1 就好，不必打印
        if row == n:
            self.res += 1
            return
        '''
        整体循环就是从这里开始。 从第一行开始放皇后，以此每一行只能放一个。
        那么 列就从（第一行）的开始到最后，即col from 0 to n-1
        用回溯的方法，比如放第一行第一列皇后，看看能否放。
        如果可以，放第二行，第一列，第二列，以此类推。
        如果不行就回溯，放第一行第二列皇后，然后第二行第一列，
        等等，直到最后一行，写入答案。
        '''
        for col in range(n):
            # 经典回溯方法，丢一个候选皇后的列进去候选结果，
            # 进入下一行，跑一跑，回撤候选皇后，继续找。
            if self.is_valid(row, col):
                self.board[row] = col
                self.solve_line(row + 1, n)
                self.board[row] = 0

    def is_valid(self, row, col):
        # 对于当前行和列，有这么几种情况是冲突的，
        # 即所有此行此列的，两个对角线的都不符合
        for i in range(row):
            # 此列已经冲突，不考虑行，因为每次都是row+1，自动跳过本行
            if self.board[i] == col:
                return False
            '''
            对于当前行和列，row + col, 这个点的对角线有两个。
            左上到右下A和左下到右上B
            对于A类型，row + col 是个常数，对于B类型，row - col 是个常数
            所以只要当前循环中的各个组合是常数之一，就不符合（不能放！）
            由于i 表示每一行，self.board[i] 是当前行的列（候选皇后的位置）
            因此就可以判断 当前组合是否是那两个常数。
            '''
            if i + self.board[i] == row + col or i-self.board[i] == row-col:
                return False
        return True

