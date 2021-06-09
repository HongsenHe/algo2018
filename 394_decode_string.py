class Solution:
    def decodeString(self, s: str) -> str:
        # Time, Space = O(n)
        # 递归
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



        # 迭代方法
        stack = []
        res, multi = "", 0
        
        for c in s:
            # 如果[, 则把multi和当前结果放入sk, 并且reset，因为进入下一层
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            # 如果], 则结束了当前层，即弹出结果并且累加
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            # 如果是数字，则累加
            elif c.isdigit():
                multi = multi * 10 + int(c)     
            # 如果是字母，则加入结果集
            else:
                res += c
        return res
