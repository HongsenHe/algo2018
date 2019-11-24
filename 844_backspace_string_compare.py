class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # by using stack
        def helper(arr):
            sk = []
            for a in arr:
                if a == '#':
                    if sk:
                        sk.pop()
                else:
                    sk.append(a)
            return sk
        return helper(S) == helper(T)
       