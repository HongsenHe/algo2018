class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic_s = {}
        dic_g = {}
        A = B = 0
        
        '''
        看了N多答案，终于自己怼出来。。。
        要分两步走，第一个for只考虑同位置的情况，并且记录不同位置数字的个数
        第二部就loop guess dict, 看是否在dic_s里，如果有就取最小值。
        比如1123和0111:
        dic_s = {1:1, 2:1, 3:1} 即 1, 2, 3分别有一个
        dic_g = {0:1, 1:2}, 但dic_s里只有一个1，所以B只能是min(1, 2)
        
        '''
        for i in range(len(secret)):
            s = secret[i]
            g = guess[i]
            
            if s == g:
                A += 1
            else:
                dic_s[s] = dic_s.get(s, 0) + 1
                dic_g[g] = dic_g.get(g, 0) + 1
                
        for k, v in dic_g.items():
            if k in dic_s:
                B += min(dic_s[k], v)
            
        return "{}A{}B".format(A, B)
        