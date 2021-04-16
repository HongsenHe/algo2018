class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        继续使用经典二分模板。
        通常来讲sorted array, mid <= right的值。
        也就是最小值在left - mid部分，也就是压缩right部分，即right = mid
        如果mid > right的值，则被rorated了，需要压缩left部分，即left = mid
        
        最后求出两个临界点，然后比较二者。经典模板应用。
        '''
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
                
        return min(nums[left], nums[right])
            
            