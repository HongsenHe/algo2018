class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k <= 1:
            return 0
        res = 0
        prod = 1
        left = 0
        
        for right in range(len(nums)):
            num = nums[right]
            prod *= num
            
            while prod >= k:
                # keep poping left pointer, move to +1, resize the window
                prod = prod // nums[left]
                left += 1
            res += right - left + 1
        
        return res