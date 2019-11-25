class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        k = len(B) // len(A)
        while len(A) * k <= 10000:
            if B in A * k:
                return k
            k += 1
        return -1