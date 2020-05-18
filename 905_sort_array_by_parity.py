class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        j = -1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                j += 1
                A[i], A[j] = A[j], A[i]
        return A
        