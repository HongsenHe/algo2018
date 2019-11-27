class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
    
        while dividend >= divisor:
            '''
            dividend = 25, divisor = 3
            25 >= 6, tmp = 6, val = 2
            25 >= 12, tmp = 12, val = 4
            25 >= 24, tmp = 24, val = 8
            
            '''
            tmp, val = divisor, 1
            while dividend >= tmp + tmp:
                # speed up, double divisor
                tmp += tmp
                val += val
            res += val
            dividend -= tmp

        if not sign:
            res = -res

        return min(max(-2147483648, res), 2147483647)