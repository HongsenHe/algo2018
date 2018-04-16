# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        '''
        again, calculate current level value x weight, 
        but get maxDepth first, then each level using maxDepth - 1
        '''
        maxDepth = self.maxDepth(nestedList, 1)
        return self.helper(nestedList, maxDepth)
        
    def helper(self, nestedList, maxDepth):
        res = 0
        for each in nestedList:
            if each.isInteger():
                res += each.getInteger() * maxDepth
            else:
                res += self.helper(each.getList(), maxDepth-1)
        return res
    
    
    def maxDepth(self, nestedList, depth):
        maxD = depth
        for each in nestedList:
            if not each.isInteger():
                # compare current maxD and next level depth (if exists)
                maxD = max(maxD, self.maxDepth(each.getList(), depth+1))
        return maxD
