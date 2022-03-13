class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_map = Counter(list(secret))
        bull_cnt = 0
        cow_cnt = 0
        
        '''
        03122022
        如果猜对了cow，则要从map 删除一个secret值，即secret_map[cur_elem] -= 1
        但这样会影响猜对bull的结果。因为删除的那个字母可能就是bull. 
        
        所以要走两遍，第一遍是只看值一样的，第二遍才是 剩下，值一样但位置不同的。
        '''
        
        # 只看值一样的，走一遍
        for i in range(len(guess)):
            cur_elem = guess[i]
            if cur_elem != secret[i]:
                continue
                
            secret_map[cur_elem] -= 1
            bull_cnt += 1
        
        # 看值不一样的
        for i in range(len(guess)):
            cur_elem = guess[i]
            if cur_elem == secret[i]:
                continue
                
            # 完全不在的，即瞎猜的，略
            if cur_elem not in secret_map:
                continue
                
            if secret_map[cur_elem] > 0:
                secret_map[cur_elem] -= 1
                cow_cnt += 1
        
        return str(bull_cnt) + 'A' + str(cow_cnt) + 'B'
                
        



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
        