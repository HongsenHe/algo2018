class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            res_a = res_b = 0
            for i in range(n):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    res_a += 1
                elif B[i] != x:
                    res_b += 1
            return min(res_a, res_b)
        
        n = len(A)
        res = check(A[0])
        if res != -1 or A[0] == B[0]:
            return res
        else:
            return check(B[0])
                
            
        