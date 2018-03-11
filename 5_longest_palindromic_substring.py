class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        '''
        这道题是比较常考的题目，求回文子串，一般有两种方法。 第一种方法比较直接，
        实现起来比较容易理解。基本思路是对于每个子串的中心（可以是一个字符，或者
        是两个字符的间隙，比如串abc,中心可以是a,b,c,或者是ab的间隙，bc的间隙）
        往两边同时进行扫描，直到不是回文串为止。假设字符串的长度为n,那么中心的个数
        为2*n-1(字符作为中心有n个，间隙有n-1个）。对于每个中心往两边扫描的复杂度
        为O(n),所以时间复杂度为O((2*n-1)*n)=O(n^2),空间复杂度为O(1)，代码如下：
        '''
        res = ''
        
        # n letter + n-1 space = 2n-1
        cyc = 2 * len(s) - 1
        for i in range(cyc):
            l = i/2
            r = i/2
            # if current cursor is in space, then split
            if i%2 == 1:
                r += 1
            
            subStr = self.helper(s, l, r)
            if len(subStr) > len(res):
                res = subStr
                
        return res
        
    def helper(self, s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
            
        return s[l+1:r]