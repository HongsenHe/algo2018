class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hm = {}
        res = 0
        
        for a in A:
            for b in B:
                hm[a + b] = hm.get((a + b), 0) + 1
                
        for c in C:
            for d in D:
                target = -(c + d)
                if target in hm:
                    res += hm[target]
                    
        return res
        