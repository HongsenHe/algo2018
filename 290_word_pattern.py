class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_str = {}
        str_to_pattern = {}
        strs = s.split(" ")
        
        '''
        对应关系不能是 a, b 对应 dog, 所以需要用key=dog, value 是唯一值
        也不能a对应dog, cat, 用key = a, value是唯一值。
        所以用两个map来表示
        '''
        
        if len(pattern) != len(strs):
            return False
        
        match = True
        for i in range(len(pattern)):
            pattern_char = pattern[i]
            str1 = strs[i]
            
            # 如果pattern不在pattern_to_str字典中，加入字典；如果冲突则不匹配
            if pattern_char not in pattern_to_str:
                pattern_to_str[pattern_char] = str1
            elif pattern_to_str[pattern_char] != str1:
                match = False
                break
            
            # 如果str不在str_to_pattern字典中，加入字典；如果冲突则不匹配
            if str1 not in str_to_pattern:
                str_to_pattern[str1] = pattern_char
            elif str_to_pattern[str1] != pattern_char:
                match = False
                break
        
        return match