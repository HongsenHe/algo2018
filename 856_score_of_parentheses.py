class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        '''
        如果是( 则放入stack
        如果是) 则弹出来，并且x2, 再加上top, 再怼进去
        '''
        for x in s:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()