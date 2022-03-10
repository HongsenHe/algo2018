class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.total = 0
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        '''
        如果当前的size超过了初始size， 即弹出第一个数字
        queue.pop(0), 这样queue总保持初始size-1的大小。
        保持一个窗口里，因此total要减去pop出来的数字，此操作为O(1)
        再把当前数字val 放到queue里，并且加入到total, 除以当前size即使平均数
        '''
        
        if len(self.queue) >= self.size:
            out = self.queue.pop(0)
            self.total -= out
            
        self.queue.append(val)
        self.total += val
        
        return self.total / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
        
    '''
    def __init__(self, size: int):
        self.size = size
        self.sk = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sk.append(val)
        def avg(sk):
            return sum(sk) / len(sk)
                
        if len(self.sk) < self.size:
            return avg(self.sk)
        else:
            sk2 = self.sk[-self.size:]
            return avg(sk2)
    '''

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)