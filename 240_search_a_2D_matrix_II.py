class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # time O(m * logn)
        if not matrix or not matrix[0]:
            return False
        
        j = len(matrix[0]) - 1
        for i in range(len(matrix)):
            j = self.binSearch(matrix[i], 0, j, target)
            if matrix[i][j] == target:
                return True
        return False
        
    def binSearch(self, row, start, end, target):
        while start <= end:
            mid = start + (end - start) // 2
            if row[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return end
