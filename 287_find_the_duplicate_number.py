class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         # two pointers, O(NlogN)
#         nums.sort()
        
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return nums[i]
            
        # binary search
        nums.sort()
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<mid+1: r = mid - 1
            else: l = mid + 1
        return l