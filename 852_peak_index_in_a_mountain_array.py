class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # 04152021 继续二分法模板
        left, right = 0, len(arr) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if arr[mid] <= arr[mid + 1]:
                left = mid
            else:
                right = mid
                
        if arr[left] > arr[right]:
            return left
        else:
            return right