class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        定义diff是左括号减去右括号的个数
        [min_diff，max_diff] 来记录括号差异的变化
        遇到左括号 (  则增加diff, both min_diff and max_diff
        遇到右括号 )  则减少diff, both min_diff and max_diff
        遇到*        可能是) 即min_diff-1, 可能是( 即max_diff+1
        
        当前循环结束后，如果max_diff < 0 则右括号已经多余左括号，False
        重置min_diff，如果<0, 则0
        最后看min_diff, 如果等于0说明左括号==右括号，因为*可以是空
        '''
        
        min_diff, max_diff = 0, 0
        for c in s:
            if c == '(':
                min_diff += 1
                max_diff += 1
            elif c == ')':
                min_diff -= 1
                max_diff -= 1
            else:
                min_diff -= 1
                max_diff += 1
                
            if max_diff < 0:
                return False
            min_diff = max(min_diff, 0)
        
        return min_diff == 0
        
                    
                