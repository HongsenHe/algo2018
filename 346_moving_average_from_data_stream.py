class MovingAverage:

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

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)