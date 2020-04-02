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
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            # continous raising, case 2
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # broken part, case 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
