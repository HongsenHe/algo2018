class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
                
        if i < len(nums1):
            nums.extend(nums1[i:])
        elif j < len(nums2):
            nums.extend(nums2[j:])
            
        n = len(nums)
        if n % 2 == 0:
            return float((nums[n//2-1] + nums[n//2])) / 2
        else:
            return nums[n//2]
        