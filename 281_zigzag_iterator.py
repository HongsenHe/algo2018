'''
就是取每个列表的第一个元素，可以用一个queue存放所有列表。
比如：queue = [[1,2], [3,4,5]] 然后每次都弹出来一个列表，并且取第一个值
作为返回值，如果取出之后还有元素，再放回到结尾，FIFO
* P.S. 要熟悉python iter(), next() 等
'''
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = [v for v in (v1, v2) if v]
        

    def next(self):
        """
        :rtype: int
        """
        head = self.queue.pop(0)
        res = head.pop(0)
        if head:
            self.queue.append(head)
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())