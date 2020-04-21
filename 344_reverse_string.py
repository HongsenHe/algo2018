class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1
        

    # updated 04202020
    def reverseString(self, s: List[str]) -> None:
        idx = 0
        self.helper(s, 0)
    
    def helper(self, s, idx):
        if idx >= len(s)//2:
            return
        s[idx], s[len(s)-1-idx] = s[len(s)-1-idx], s[idx]
        self.helper(s, idx+1)