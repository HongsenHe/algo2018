class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        boyer moore voting algorithm...
        pick two candidates: n1, n2 and its count c1, c2
        if current number is one of them, then count++
        if not and count is still 0, then set current number to candidates with count = 1
        else count--
    
        '''
        
        n1 = n2 = None
        c1 = c2 = 0
        
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 = 1
            elif c2 == 0:
                n2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
                
        '''
        now we have two candidates, then calculate the their counts 
        and see the condition n/3, reset count first
        '''
        c1 = c2 = 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
        
        res = []
        if c1 > len(nums) / 3:
            res.append(n1)
        if c2 > len(nums) / 3:
            res.append(n2)
            
        return res