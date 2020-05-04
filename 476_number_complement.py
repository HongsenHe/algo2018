class Solution:
    def findComplement(self, num: int) -> int:
        todo, bit = num, 1
        while todo:
            # flip current bit
            num = num ^ bit
            # prepare for the next run
            bit = bit << 1
            todo = todo >> 1
        return num