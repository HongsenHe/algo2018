class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set()
        
        while True:
            s = str(n)
            tmp = 0

            for i in range(len(s)):
                num = int(s[i])
                tmp += num * num
            if tmp == 1:
                return True
            if tmp in dic:
                return False
            dic.add(tmp)
            n = tmp