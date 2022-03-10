class MyQueue:

    def __init__(self):
        self.sk = []
        

    def push(self, x: int) -> None:
        self.sk.append(x)
        

    def pop(self) -> int:
        tmp = []
        
        while self.sk:
            tmp.append(self.sk.pop())
            
        res = tmp.pop()
        
        while tmp:
            self.sk.append(tmp.pop())
        return res
        

    def peek(self) -> int:
        tmp = []
        
        while len(self.sk) > 1:
            tmp.append(self.sk.pop())
            
        res = self.sk.pop()
        tmp.append(res)
        
        while tmp:
            self.sk.append(tmp.pop())
        return res
        

    def empty(self) -> bool:
        return len(self.sk) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()