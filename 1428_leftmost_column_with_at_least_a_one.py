# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        left = 0
        right = cols - 1
        '''
        上二分法模板。 左右指针分别用列的头和尾。
        确定列的中点后，看每一行的数字。
        如果中点是1，则舍弃右边部分。因为右边肯定都是1.
        
        最后分别看左右指针的每一行。
        
        '''
        
        while left + 1 < right:
            mid_col = (left + right) // 2
            
            flag = False
            for row in range(rows):
                if binaryMatrix.get(row, mid_col) == 1:
                    flag = True
                    break
                    
            if flag:
                right = mid_col
            else:
                left = mid_col
                
        for row in range(rows):
            if binaryMatrix.get(row, left) == 1:
                return left
            
        for row in range(rows):
            if binaryMatrix.get(row, right) == 1:
                return right
            
        return -1
                    
                
            