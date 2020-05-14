class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        sk = []
        if k == len(num):
            return "0"
        
        '''
        贪心算法和严格递增stack
        比如[143]
        如果4比stack peek 1 大，就放进去
        如果3比peek 4小，就考虑是要14 还是13， 显然13 < 14，弹出4 放入3
        即，当前元素比peek小就一直弹，每次k--, 然后放进sk。
        如果k还有数值要考虑只返回前len(num) - k项，之后的就不要了。
        '''

        for digit in num:
            while k and sk and sk[-1] > digit:
                sk.pop()
                k -= 1
            sk.append(digit)
            
        if k:
            sk = sk[:-k]
        
        return "".join(sk).lstrip('0') or "0"
            
