class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sk = []
        s = list(s)
        
        '''
        单纯看() 不理会字母。如果是( 则把相应的index放进stack
        如果是) 则看stack是否有对应的( 如果有，则继续。如果没有
        立刻改原字符串，即把当前的) 删除， s[i] = ''
        
        循环之后，如果stack还有数字，意味着有多余的(, 
        则改动原字符串，并且把这些index的值删除，即 s[i] = ''
        
        '''
        
        for i in range(len(s)):
            if s[i] == '(':
                sk.append(i)
            elif s[i] == ')':
                if sk:
                    sk.pop()
                else:
                    s[i] = ''
                    
        for i in sk:
            s[i] = ''
            
        return ''.join(s)
            
                
            