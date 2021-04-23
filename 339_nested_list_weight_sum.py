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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
#         # 此题DFS比较好
#         return self.helper(nestedList, 1)
    
    
#     def helper(self, nestedList, depth):
#         res = 0
        
#         # 此递归的出口在哪？如果当前是个纯list, 则对于每个int进行计算作为出口。
#         for node in nestedList:
#             if node.isInteger():
#                 res += node.getInteger() * depth
#             else:   
#                 res += self.helper(node.getList(), depth + 1)
            
#         return res
            
    
        # BFS 解法
        queue = collections.deque(nestedList)

        depth = 1
        total = 0

        while len(queue) > 0:
            for i in range(len(queue)):
                nested = queue.pop()
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    # 此处用这种方式
                    queue.extendleft(nested.getList())
            depth += 1

        return total

        