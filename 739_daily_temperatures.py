class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        sk = []
        for i in range(len(T)-1, -1, -1):
            '''
            if cur num > peek, discard peek
            until all of them, then push cur num into sk
            as we need find the num (peek) > cur num, so keep pop()
            until find that one
            if cur num < peek, just push and calculate the date
            base on peek (date idx) - cur date
            '''
            while sk and T[i] >= T[sk[-1]]:
                sk.pop()
            if sk:
                res[i] = sk[-1] - i
            sk.append(i)
            
        return res