class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set()
        words = set()
        
        for num1 in nums1:
            words.add(num1)
        for num2 in nums2:
            if num2 in words:
                res.add(num2)
        return list(res)
    
    
        # one line solution series
        #return list(set(nums1) & set(nums2))