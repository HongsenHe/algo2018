class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hm = {}
        res = 0
        
        '''
        一共4个tuple, 每个tuple有两个数字，排列组合一下，任意两个tuple就有4中方案，即2x2
        即, tuple_1_1 * tuple_2_1, tuple_1_2 * tuple_2_1, ...
        构成的4种方案就是4个sum, 从剩下的两个tuple里找答案，经典问题开始。。。
        
        '''
        
        for a in A:
            for b in B:
                hm[a + b] = hm.get((a + b), 0) + 1
                
        for c in C:
            for d in D:
                target = -(c + d)
                if target in hm:
                    res += hm[target]
                    
        return res
        