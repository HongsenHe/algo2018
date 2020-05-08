class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        '''
        小学斜率问题，对于(x, y) 要和(x1, y1) (x2, y2) 三个点的斜率一样。
        (x1, y1) 和 (x2, y2) 就取题中前两个点，然后for loop之后每一个点
        即 (y - y1) / (x - x1) = (y1 - y0) / (x1 - x0)
        但有可能出现x1 - x0 = 0的情况。所以稍加变换。
        即 (y - y1) * (x1 - x0) = (x - x1) * (y1 - y0)
        
        '''
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y - y1) * (x1 - x0) != (x - x1) * (y1 - y0):
                return False
        return True
                
            
            