class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #两个隔板的矮的那一个的高度乘以两个隔板的间距就是储水量。
        res = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            curArea = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            res = max(res, curArea)
        return res