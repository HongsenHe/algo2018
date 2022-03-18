class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        和题5类似，找到所有的palindromic substring。
        当前idx有两种情况分别判断。
        如果当前数字是中心，则整个substring是奇数位， 
        分别判断以当前数字为中心的两边数字，即left -= 1 vs right += 1
        
        如果substring是偶数位，则当前数字的前一个和后一个开始组成答案
        即参数是 i & i, 前一个是i & i + 1
        '''
        
        res = 0
        for i in range(len(s)):
            res += self.helper(i, i+1, s) + self.helper(i, i, s)
        return res
    
    def helper(self, i, j, s):
        count = 0
        
        # 好习惯，总把condition 写在while loop里。
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
        return count