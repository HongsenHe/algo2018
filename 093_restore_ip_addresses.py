class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        列举当前位置是否可以加. 再看是否合法化        
        '''
        result = []
        # 维护一个当前string， 一个idx (pos)， 使用dot的数量
        self.dfs(s, 0, 0, "", result)
        return result
    
    def dfs(self, s, pos, dot, cur_string, result):
        # 跳出条件，最多加三个点
        if dot > 3:
            return
        
        # 搜索到最后，判断是否合法
        if pos == len(s):
            if dot == 3:
                nums = cur_string.split('.')
                
                # 每个部分必须满足0-255 第一个可以是0 但长度不能超过1
                for num in nums:
                    if len(num) > 1 and num[0] == '0':
                        return
                    if int(num) > 255:
                        return
                # 只把正解加入结果集
                result.append(cur_string)
                return
            return 
        
        # 当前position后面不加 .
        self.dfs(s, pos + 1, dot, cur_string + s[pos], result)
        
        # 加 .
        if pos < len(s) - 1:
            self.dfs(s, pos + 1, dot + 1, cur_string + s[pos] + '.', result)