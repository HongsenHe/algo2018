# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # try:
        #     return mountain_arr._MountainArray__secret.index(target)
        # except ValueError:
        #     return -1
        
        '''
        03152022
        此题比较像33, 162和852。先找到peak方便判断单调递增的终点。
        找peak的方式参考162和852， 经典二分发模板
        找到之后判断整体，参考33是一个rotated sorted array. 
        但此题需要找第一个index， 所以使用二分法的时候，需要判断单调递增还是递减。
        如果target在递增区间，则移动right, 
        如果target > mid_val, 并且是递增区间, 则移动left, 总体分四种情况考虑。
        分别在0 - peak 和 peak - end 寻找target。
        
        经典二分模板:
        left + 1 < right, 然后分别判断left, right的值和target的关系。
        '''
        peak = self.find_peak(mountain_arr)
        # binary search for increasing part (0 to peak)
        res = self.bin_search(0, peak, mountain_arr, target, True)
        
        if res == -1:
            # binary search for decreasing part (peak to the end)
            res = self.bin_search(peak, mountain_arr.length() - 1, mountain_arr, target, False)
        
        return res
    
    def bin_search(self, left, right, mountain_arr, target, is_ascending):
        while left + 1 < right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            
            if mid_val == target:
                return mid
            
            if mid_val < target:
                if is_ascending:
                    left = mid
                else:
                    right = mid
            elif mid_val > target:
                if is_ascending:
                    right = mid
                else:
                    left = mid
        
        if mountain_arr.get(left) == target:
            return left
        if mountain_arr.get(right) == target:
            return right
        return -1 
            
        
    def find_peak(self, mountain_arr):
        left = 0
        right = mountain_arr.length() - 1
        
        while left + 1 < right:
            mid = (left + right) // 2 
            if mountain_arr.get(mid) <= mountain_arr.get(mid + 1):
                left = mid
            else:
                right = mid
                
        if mountain_arr.get(left) > mountain_arr.get(right):
            return left
        
        return right