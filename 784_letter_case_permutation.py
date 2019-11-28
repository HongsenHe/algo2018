class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.helper(res, '', S.lower(), 0)
        return res
    
    def helper(self, res, each, S, start):
        if start == len(S):
            res.append(each)
            return
            
        # itself, could be digit or lower case
        self.helper(res, each + S[start], S, start+1)
        if 'a' <= S[start] <= 'z':
            # if char, use upper()
            self.helper(res, each + S[start].upper(), S, start+1)
        