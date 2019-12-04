class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while left <= right:
            mid = left + (right-left) // 2
            sq = mid * mid
            
            if sq < x:
                left = mid + 1
            elif sq > x:
                right = mid - 1
            else:
                return mid
        
        return right

# class Solution:
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         start = 1
#         end = x
        
#         # find the last number which < x
#         while start + 1 < end:
#             mid = start + (end-start) // 2
#             if mid * mid <= x:
#                 start = mid
#             else:
#                 end = mid
#         if end * end <= x:
#             return int(end)
#         return int(start)
        