class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) > len(nums1):
            return self.intersect(nums2, nums1)
        
        ct = collections.Counter(nums1)
        res = []
        for num2 in nums2:
            if ct[num2] > 0:
                res.append(num2)
                ct[num2] -= 1
        return res