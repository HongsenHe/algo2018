class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 1. reverse the whole string
        self.reverse(0, len(s)-1, s)

        # 2. reverse each word in the whole string
        start, end = 0, 0
        while start < len(s):
            # find the space index
            while end < len(s) and s[end] != ' ':
                end += 1
        
            # reverse this single word
            self.reverse(start, end-1, s)
            
            # at this point, end is space, start should be next
            start = end + 1
            # also end should be next, and keep going until start hit the end
            end += 1
        
        
    def reverse(self, left, right, s):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1