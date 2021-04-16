class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time: O(m + n)
        m = len(matrix)
        n = len(matrix[0])
        
        i = m - 1
        j = 0
        
        while i >= 0 and j < n:
            cur = matrix[i][j]
            
            if target == cur:
                return True
            elif target > cur:
                j += 1
            else:
                i -= 1
        return False    

#         # binary search, Time = O(mlogn)
#         if not matrix or not target:
#             return False
        
#         m = len(matrix)
#         n = len(matrix[0])
#         j = n - 1
        
#         for i in range(m):
#             j = self.bin_search(matrix[i], target, 0, j)
            
#             if matrix[i][j] == target:
#                 return True
#         return False
    
#     def bin_search(self, row, target, start, end):
#         while start <= end:
#             mid = (start + end) // 2
#             if row[mid] > target:
#                 end = mid - 1
#             else:
#                 start = mid + 1
                
#         return end
        '''
        不断逼近，从左下角开始。
        如果target比当前数字大，则向右走，因为右边的数字大于当前。
        如果target比当前数字小，要向上走，因为向上是递减的。
        
        
        '''
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            