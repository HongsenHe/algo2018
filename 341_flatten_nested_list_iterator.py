# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        '''
        算是stack题目
        先把nestedList翻转倒进stack里，
        这样stack.pop就是nestedList第一个元素了
        '''
        self.stack = list(reversed(nestedList))
        
    def next(self):
        # 拿下一个元素，即stack.pop，看看是不是int type
        return self.stack.pop().getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        '''
        如何检查是否有next? 
        遍历一下stack, 如果它的顶top 是int type了，那肯定有，返回True
        如果是list type, 则需要重新构建stack一下 (flatten process)
        即，stack之前的元素（除了最后一个list 元素) 加上
        最后一个list元素的倒序，即使新的stack
        
        继续循环stack, 直到返回int type
        '''
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:len(self.stack)-1]+top.getList()[::-1]
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())