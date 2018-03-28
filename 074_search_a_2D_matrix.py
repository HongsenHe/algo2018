class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''        
        if not matrix:
            return False
        if not matrix[0]:
            return False
        # find which row
        up = 0
        down = len(matrix) - 1
        while up + 1 < down:
            mid = up + (down - up) // 2 
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                up = mid
            else:
                down = mid
        
        rowIdx = 0 
        if matrix[down][0] > target:
            rowIdx = up
        else:
            rowIdx = down
        row = matrix[rowIdx]
        
        # find which column, the answer
        left = 0
        right = len(row) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid
            else:
                right = mid
        if row[left] == target or row[right] == target:
            return True
        return False
        '''
        # a good solution from discuss
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows * cols - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            value = matrix[mid // cols][mid % cols]
            
            if value == target:
                return True
            elif value < target:
                start = mid + 1
            else:
                end = mid - 1
        return False