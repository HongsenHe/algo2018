class Solution:
    def longestPalindrome(self, s: str) -> int:
        # if find char in pool set, add this pair (2) into res
        # then remove, after loop, add the 'mid' one
        pool = set()
        res = 0
        for c in s:
            if c in pool:
                pool.remove(c)
                res += 2
            else:
                pool.add(c)
        if len(pool) > 0:
            res += 1
        return res
            