class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        the key point is the make sure where is the mid pts. 
        so compare left with mid value
        make sure it's continuous rising, then use binary search.
        
        case 1       / |            case 2    /   |
                    /  |                     /    |
                    ---|----   or           / ----|-----
                       |  /                       |  /     
                       | /                        | /   
                       |/                         |
                [4, 5, 1, 2, 3]             [3, 4, 5, 1, 2]
        
        '''
        # 04152021, 套用模板，用 left + 1 < right, 先判断大的升序降序，再小范围找
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            # 升序 case2, 找出单调递增再缩小范围
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        
        # 找到分界点后分别判断
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        
        return -1
        
