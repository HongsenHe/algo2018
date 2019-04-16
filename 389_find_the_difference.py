class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        dic = {}
        for s1 in s:
            if s1 in dic:
                dic[s1] += 1
            else:
                dic[s1] = 1
        
        for t1 in t:
            if t1 in dic:
                if dic[t1] == 0:
                    return t1
                else:
                    dic[t1] -= 1
            else:
                return t1
        '''
            
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1