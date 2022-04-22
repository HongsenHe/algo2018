class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return ['']
        queue = deque([s])
        result, visited = [], set([s])
        found = False
        
        while queue:
            cur = queue.popleft()
            if self.is_valid(cur):
                found = True
                result.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i + 1:]
                        if t not in visited:
                            queue.append(t)
                            visited.add(t)
        return result
        
        
        
    def is_valid(self, s):
        '''
        写一个基础函数。判断字符串是否是合法。
        撸一遍字符串，如果是左括号，则cnt + 1
        如果是右括号，则cnt - 1
        最后cnt应该是0，即平衡状态
        '''
        cnt = 0
        
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    return False
                
                cnt -= 1
                
        return cnt == 0
                