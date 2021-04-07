class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        left = 0
        right = len(s) - 1
        
        while left <= right:
            # 如果发现不相等，有两种情况。 1. skip left 数字也就是 left + 1, 或者省略right 数字
            if s[left] != s[right]:
                return self.valid(s, left + 1, right) or self.valid(s, left, right - 1)
            
            # 如果当前left, right一样，继续走。
            left += 1
            right -= 1
            
        return True
    
    
    def valid(self, s, left, right):
        # 纯粹的判断此字符串s 是否是palindrome
        while left <= right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True