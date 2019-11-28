class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # if palindrome, every char should be even number
        # except only one char can be 1
        pool = set()
        for c in s:
            if c in pool:
                pool.remove(c)
            else:
                pool.add(c)
        return len(pool) <= 1