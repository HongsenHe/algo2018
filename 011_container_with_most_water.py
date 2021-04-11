class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        思考为什么不是同向双指针，而是相向双指针。
        木桶原理：面积就是较短的木版min(left, right) 乘以他们的间距 right - left
        然后打擂台和全局比较。如果哪个木版较短就移动他。直到双指针相会。
        '''
        
        left, right = 0, len(height) - 1
        res = float('-inf')
        
        while left <= right:
            area = min(height[left],  height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
            res = max(res, area)
            
        return res
            