class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        n = len(board) # should be 9
        
        # no duplicated number for each row and column
        for row in board:
            if not self.valid(row):
                return False
        for col in zip(*board):
            if not self.valid(col):
                return False
        # no dplicated number for sub board 3 x 3 
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                nums = []
                for x in range(i, i+3, 1):
                    for y in range(j, j+3, 1):
                        nums.append(board[x][y])
                if not self.valid(nums):
                    return False
        return True
    
    def valid(self, nums):
        # if no duplicated number, then it's valid
        nums = [num for num in nums if num != '.']
        return len(nums) == len(set(nums))