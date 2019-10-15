class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        
        res = 0
        while x != 0:
            a = x%10
            x = x//10
            res = res*10 + a
        
        if res > pow(2, 31) -1 or res < -pow(2, 31):
            return 0
        return res