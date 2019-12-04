class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        for i in range(2000):
            if pow(2, i) == n:
                return True
        return False
        '''
        
        return n != 0 and n & (n - 1) == 0