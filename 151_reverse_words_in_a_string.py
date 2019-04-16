class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))
        
    def reverseWords(self, s: str) -> str:
        s = s.split()
        l = len(s)
        for i in range(l//2):
            tmp = s[i]
            s[i] = s[l-i-1]
            s[l-i-1] = tmp
        return ' '.join(s)