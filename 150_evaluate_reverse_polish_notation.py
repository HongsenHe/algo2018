class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sk = []
        ops = ['+', '-', '*', '/']
        
        for token in tokens:
            if token not in ops:
                sk.append(int(token))
            else:
                first = sk.pop()
                second = sk.pop()
                res = 0
                if token == '+':
                    res = second + first
                elif token == '-':
                    res = second - first
                elif token == '*':
                    res = second * first
                elif token == '/':
                    res = second / first
                sk.append(int(res))
        return sk[-1]
                        
                