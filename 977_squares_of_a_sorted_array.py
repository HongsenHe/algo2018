class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # solution 1: square then sort, time O(NlgN)
        # res = []
        # for a in A:
        #     res.append(a*a)
        # return sorted(res)
        
        # solution 2: try one line solution :D 
        # return sorted([a * a for a in A])
        
        # solution 3: two pointers
        i = 0
        j = len(A) - 1
        res = []
        
        while i <= j:
            if abs(A[i]) >= abs(A[j]):
                res.insert(0, A[i] * A[i])
                i += 1
            else:
                res.insert(0, A[j] * A[j])
                j -= 1
        return res