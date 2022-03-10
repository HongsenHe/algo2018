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
        # 03092022
        # 初始化的时候，避免其中一个为None, 这样再叫next的时候
        # 则避免head.pop(0)的情况，一旦进入next, 则有if head判断
        if not v1:
            self.queue = [v2]
        elif not v2:
            self.queue = [v1]
        else:
            self.queue = [v1, v2]
        
        

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


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.total = len(v1) + len(v2)
        self.cur = 0
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        def prt_v(v, idx):
            return v[idx]

        res = 0
        self.cur += 1

        # special check, if any empty go another
        # then if odd go v1, even go v2
        if self.i == len(self.v1):
            res = prt_v(self.v2, self.j)
            self.j += 1
        elif self.j == len(self.v2):
            res = prt_v(self.v1, self.i)
            self.i += 1
        elif self.cur % 2 == 1:
            res = prt_v(self.v1, self.i)
            self.i += 1
        elif self.cur % 2 == 0:
            res = prt_v(self.v2, self.j)
            self.j += 1

        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur < self.total
        
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())