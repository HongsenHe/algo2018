class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sk = []
        self.minSk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.sk.append(x)
        # only push the element is smaller than minSk or init
        if len(self.minSk) == 0 or x <= self.minSk[-1]:
            self.minSk.append(x)

            
    def pop(self):
        """
        :rtype: void
        """
        # when pop, if current ele is min value, then pop from minSk
        if self.top() == self.getMin():
            self.minSk.pop()
        return self.sk.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.sk[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minSk[-1]
    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()