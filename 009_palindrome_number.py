class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        b = x
        res = 0
        while x != 0:
            a = x % 10
            res = res * 10 + a
            x = x // 10
            
        return res == b
            
        