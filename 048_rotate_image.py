class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                # left_but: going up (n-1-j), but same col until next outter loop col+1
                tmp = matrix[n-1-j][i]
                # need right_but: going left (n-1-j), but same row until next outter loop n-1-i
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                # need right_top: going down (j), but same col until next outter loop n-1-i
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                # need left_top: going right (j), but same col until next outter loop row+1
                matrix[j][n-1-i] = matrix[i][j]
                # need left_but, tmp
                matrix[i][j] = tmp
