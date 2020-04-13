class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        # 为了方便，保持s长度小于t
        if m > n:
            return self.isOneEditDistance(t, s)
        # 如果长度大于一 或者一样，则不满足条件
        if abs(m-n) > 1 or s == t:    
            return False

        """
        case 1: ab和cab比较，后者多了一个c, 
        如果满足条件，则看除去这个c, 是否两组字符相等，
        也就是看后者[i+1:] 和前者比较
        
        case 2: ab和cb比较，当前不一样，看之后的所有是否相同
        也就是比较s[i+1:] 和 t[i+1:]
        """
        for i in range(m):
            if s[i] != t[i]:
                return s[i:] == t[i+1:] or s[i+1:] == t[i+1:]
        return True