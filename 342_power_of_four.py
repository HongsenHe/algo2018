from math import log2

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # if num < 1:
        #     return False
        # while num % 4 == 0:
        #     num /= 4
        # return num == 1
        return num > 0 and log2(num) % 2 == 0
        