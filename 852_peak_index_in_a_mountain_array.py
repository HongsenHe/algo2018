class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
                
        