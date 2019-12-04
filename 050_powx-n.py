class Solution:
    def myPow(self, x: float, n: int) -> float:
        # solution 1
        '''
        if n < 0:
            x = 1/x
            n = -n
        res = 1
        for i in range(n):
            res = res * x
        return res
        '''
        
        # solution 2, time O(logn), space O(logn)
        if n < 0:
            x = 1/x
            n = -n
        return self.helper(x, n)
    
    def helper(self, x, n):
        if n == 0:
            return 1.0
        half = self.helper(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x