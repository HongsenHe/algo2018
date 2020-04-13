class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        hm = {0 : 1}
        res = 0
        pre_sum = 0
        '''
        if a % k == b % k, then (a - b) % k == 0
        求每次的积累，如果这个pre_sum 能在hm里找到
        即 (pre_sum + a) % k == (pre_sum) % k
        即 (pre_sum + a - pre_sum) % k == 0
        即 a % k == 0 
        所以加上之前的答案到res
        '''
        for a in A:
            pre_sum = (pre_sum + a) % K
            if pre_sum in hm:
                res += hm[pre_sum]
            hm[pre_sum] = hm.get(pre_sum, 0) + 1
        
        return res
        