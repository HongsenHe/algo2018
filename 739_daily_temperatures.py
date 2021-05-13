class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        用stack的思想。从后向前走！不断构建stack，把大的数字的index
        放进stack里，依次比较。
        如果当前数字比stack peek大，就弹出来，一直弹到当前数字是最大的。
        如果此时stack不是空，则算距离，stack保存每个数对应的index， 
        所以和当前i比较。
        最后再吧当前数字的index 放到stack中。
        '''
        
        res = [0 for _ in range(len(temperatures))]
        sk = []
        
        for i in range(len(temperatures) - 1, -1, -1):
            while sk and temperatures[i] >= temperatures[sk[-1]]:
                sk.pop()
                
            if sk:
                res[i] = sk[-1] - i
            
            sk.append(i)
        
        return res