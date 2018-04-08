import sys
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "":
            return 0
        i = 0
        sign = 1
        res = 0
        length = len(str)
        MaxInt = (1 << 31) - 1
        
        # check first index(i) is a positive or negative sign or no-sign
        if str[0] == '+':
            i += 1
        elif str[0] == '-':
            i += 1
            sign = -1
            
        # calculate each character, if bigger than big, return maxInt
        for i in range(i, length):
            cur = str[i]
            if cur < '0' or cur > '9':
                break
            res = res * 10 + int(cur)
        res *= sign
        
        if res >= MaxInt:
            return MaxInt
        if res < MaxInt * -1:
            return MaxInt * -1 - 1
        return res