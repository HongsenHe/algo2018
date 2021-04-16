class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        up, down = 0, m - 1
        
        while up + 1 < down:
            mid = (up + down) // 2
            
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                up = mid
            else:
                down = mid
            
        row_idx = 0
        # 找到第一列的两个指针进行比较，如果down比target大，
        # 那么压缩下半部分，使用up行
        if matrix[down][0] > target:
            row_idx = up
        else:
            row_idx = down
            
        arr = matrix[row_idx]
        left, right = 0, n - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid
            else:
                right = mid
    
        # 找到这一行的两个指针进行分别比较。
        if arr[left] == target or arr[right] == target:
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
        '''