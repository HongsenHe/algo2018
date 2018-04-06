class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or not k:
            return False
        hm = {}
        for i, num in enumerate(nums):
            if num in hm and abs(hm[num] - i) <= k:
                return True
            hm[num] = i
        return False
            