class MaxStack:

    def __init__(self):
        self.sk = []
        self.max_sk = []
        

    def push(self, x: int) -> None:
        if self.max_sk:
            self.max_sk.append(max(self.max_sk[-1], x))
        else:
            self.max_sk.append(x)
            
        self.sk.append(x)

    
    def pop(self) -> int:
        self.max_sk.pop()
        return self.sk.pop()
        

    def top(self) -> int:
        return self.sk[-1]

    
    def peekMax(self) -> int:
        return self.max_sk[-1]
        

    def popMax(self) -> int:
        max_val = self.max_sk[-1]
        tmp = []
        
        while max_val != self.sk[-1]:
            tmp.append(self.sk.pop())
            self.max_sk.pop()
            
        self.sk.pop()
        self.max_sk.pop()
        
        for num in tmp[::-1]:
            self.push(num)
            # self.max_sk.push(num)

        return max_val
    


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()