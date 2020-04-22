class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
#         dp = [[1] * (i+1) for i in range(rowIndex+1)]
#         for i in range(rowIndex+1):
#             for j in range(1, i):
#                 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
#         return dp[-1]

        '''
        先定义要输出的长度也就是n+1个[1] [1,1,1,1,1]
        然后从上到下，从右到左的累加，只保存当前的，根据上一层的数字计算
        第一层就是1，所以i从 idx=1开始
        比如i = 2 row = [1, 3, 3, 1, 1]
        接下来i = 3 j从3到1，因为第一个元素总是1 (idx=0), 
        row[3] 就等于之前的加上现在的row[3-1]+row[3] 也就是3+1 = 4
        row[2] = row[2-1] + row[2] = 3 + 3 = 6
        row[1] = row[1-1] + row[1] = 1 + 3 = 4
        因此就是[1, 4, 6, 4, 1]
        '''
        row = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j-1]
        return row