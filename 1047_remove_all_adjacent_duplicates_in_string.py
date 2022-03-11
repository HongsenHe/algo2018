from collections import deque

class Solution:
    def removeDuplicates(self, s: str) -> str:
        sk = deque()
        
        '''
        消除元素问题，可以用stack表达，和匹配括号相似。(){}[]
        如果当前元素和stack 的top 一样，则消除，即stack.pop()
        否则插入stack
        '''
        
        for c in s:
            if sk and c == sk[-1]:
                sk.pop()
            else:
                sk.append(c)
        
        return ''.join(sk)
            
            