class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(i):
            # 每次进入一层就reset这些参数
            res, multi = "", 0
            
            # 不用for loop, 会乱
            while i < len(s):
                c = s[i]
                
                # 遇到数字则累加，因为有的数字是两位以上
                if c.isdigit():
                    multi = multi * 10 + int(c)
                # 开始递归
                elif c == '[':
                    '''
                    传入i+1来获得字母。目标是获得[]里的内容，当遇到 ]的时候，
                    则返回它的i, 即更新当前层的i 让循环继续。
                    举例: 3[a]2[bc]， 当前i = 1, 进入dfs计算, 把第一个字母a
                    加入res里，继续走，到达]的时候跳出，此时附上它的i = 3返回
                    到i = 1层，并且更新，即i = 3, 而且res= 3 x 返回值tmp (a)
                    此层操作结束，reset multi
                    '''
                    i, tmp = dfs(i + 1)
                    res += multi * tmp
                    multi = 0
                elif c == ']':
                    return i, res
                else:
                    # 遇到字母则加入
                    res += c
                    
                i += 1
                
            return res
        
        
        return dfs(0)