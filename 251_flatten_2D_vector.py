class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.queue = []
        for vec in vec2d:
            if vec:
                self.queue.append(vec)
            

    def next(self):
        """
        :rtype: int
        """
        head = self.queue.pop(0)
        res = head.pop(0)
        
        if head:
            self.queue.insert(0, head)
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())