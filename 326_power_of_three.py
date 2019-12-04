class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # time: O(log3N)
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
        