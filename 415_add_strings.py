class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s = ''
        carry = 0
        cur = 0
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 or j >= 0 or carry:
            cur = carry
            if i >= 0:
                cur += int(num1[i])
            if j >= 0:
                cur += int(num2[j])

            carry, rem = divmod(cur, 10)
            
            i -= 1
            j -= 1
            
            s = str(rem) + s

        return s
