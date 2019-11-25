class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(0, len(s)):
            sub_str = s[0:i + 1]
            n = len(sub_str)
            for j in range(i + 1, len(s), n):
                if sub_str != s[j:j+n] or j+n > len(s):
                    break
                if sub_str == s[j:j + n] and j+n == len(s):
                    return True
        return False