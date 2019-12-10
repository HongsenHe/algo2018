class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zero = set()
        col_zero = set()
        
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        # for row in row_zero:
        #     for i in range(n):
        #         matrix[row][i] = 0
        # for col in col_zero:
        #     for j in range(m):
        #         matrix[j][col] = 0
        
        for i in range(m):
            for j in range(n):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
            
        