class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """    
        # from here:
        # http://bookshadow.com/weblog/2015/08/12/leetcode-zigzag-conversion/
        if numRows == 1 or numRows >= len(s):
            return s
        zigzag = [[] for x in range(numRows)]
        row, step = 0, 1
        for c in s:
            zigzag[row] += c,
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(reduce(operator.add, zigzag))