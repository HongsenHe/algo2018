class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''
        matrix pre sum的问题，通用公式
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1] 
        '''
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        self.dp = [[0] * cols for j in range(rows)]        
        
        for i in range(1, rows):
            for j in range(1, cols):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1] 

                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]                
                
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)