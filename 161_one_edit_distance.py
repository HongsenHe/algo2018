class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        # 总保持s的长度是小于t的，方便计算
        if m > n:
            return self.isOneEditDistance(t, s)
        # 如果他们长度差大于一了或者压根就相等，怎么也玩不转
        if abs(m-n) > 1 or s == t:
            return False
        
        for i in range(m):
            '''
            已经出现第一次不相等，之后的字符一定要相等，这里可能是插入或者替换
            举例a和ba，那就看之后的如果是插入一个字符(b), 那s当前之后的字符要和t之后的字符相等
            举例ac和bc，这里是替换，那s当前之后的字符要和t当前之后的字符相等
            '''
            if s[i] != t[i]:
                return s[i:] == t[i+1:] or s[i+1:] == t[i+1:]
        return True