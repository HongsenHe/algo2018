class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        '''
        a slow pointer k marks the first 'val' position 
        and changes value with faster pointer
        '''
        
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # assign current value to slow pointer
                # as sp postion is marking the first 'val'
                nums[k] = nums[i]
                k += 1
            # else keep moving the faster pointer until find a diff value
            # must keep the slower in place
        return k
                
        