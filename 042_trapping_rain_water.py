class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        也是相向型双指针问题。
        盛水的关键在于左右都有挡着，并且中间是凹进去的。
        左右的挡板也有大小之分，根据木桶原理，如果左木版比较矮，
        先求左边的盛水，即max_left - cur_left，然后移动指针left += 1
        如果当前木版大于max_left， 则更新，即 max_left = max(max_left, height[left])
        同理如果左边比右木版大了，求右边木版，更新总答案。直到相遇。
        
        '''
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        max_left = height[left]
        max_right = height[right]
        res = 0
        
        while left <= right:
            if max_left < max_right:
                max_left = max(max_left, height[left])
                res += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                res += max_right - height[right]
                right -= 1
                
        return res
            
            