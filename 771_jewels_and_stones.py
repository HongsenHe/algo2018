class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)
        '''        
        res = 0 
        for s in S:
            if s in J:
                res += 1
        return res
        '''