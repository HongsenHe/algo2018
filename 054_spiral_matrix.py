class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        first_row = 0
        first_col = 0
        res = []
        
        while rows > 0 and cols > 0:
            # define the boundary 
            last_row = first_row + rows - 1
            last_col = first_col + cols - 1
            
            # top left to right, start from first_row and first_col adding by i
            for i in range(cols):
                res.append(matrix[first_row][i+first_col])
            
            # right top to bottom, start from first_row and last_col adding by i
            for i in range(1, rows):
                res.append(matrix[first_row+i][last_col])

            # bottom right to left, start from last_row and last_col minusing by i
            for i in range(1, cols):
                # ignore same row
                if first_row != last_row:
                    res.append(matrix[last_row][last_col-i])
                
            # left bottom to top, start from last_row and first_col minusing by i
            for i in range(1, rows-1):
                # ignore same col
                if first_col != last_col:
                    res.append(matrix[last_row-i][first_col])
                
            # every layer, total rows and cols will - 2
            rows -= 2
            cols -= 2
            
            # every layer, first_row and first_col + 1
            first_row += 1
            first_col += 1
            
        return res
                
            
        