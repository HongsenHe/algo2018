class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        hm = {0: 1}
        
        '''
        [3, 4, 7, 2, -3, 1, 4, 2], k = 7
        可以理解为2sum 问题，设当前index=i, 一个是i之前的累加(包括i)，另一个是i本身的数字
        如果相加就是k 即找到。
        比如i = 2, 前面累加的total = 3 + 4 + 7 = 14. 另一个本身是7，刚好k = 7
        也就是在hm里可以找到，即 total - k in hm. 把答案放入结果中。
        
        如果当前的累加没有在hm出现，也要14加入hm，以便后面继续计算。如果14已经在hm里。
        则hm的value 要 +1. 证明有两组答案。比如
        3 4 7 and 3 4 7 2 -3 1都可以。
        2sum - hashmap的思想，把前面的累加看成一个因数，当前数字是另一个。
        
        
        '''
        for num in nums:
            total += num
            
            if total - k in hm:
                res += hm[total - k]
            
            hm[total] = hm.get(total, 0) + 1
            
        return res
            
                
            