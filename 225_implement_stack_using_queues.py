class MyStack:
    # 03082022, push O(n), pop O(1)
    def __init__(self):
        self.q1 = []
        

    def push(self, x: int) -> None:
        tmp = []
        tmp.append(x)
        
        '''
        此处构造一个stack, 举例：
        进来一个1，则 当前q1 = [1]
        进来2， 则当前tmp = [2], 再把q1 转移过来，即[2, 1]
        进来3， 当前tmp = [3], 把q1 [2, 1]转移过来。变成[3, 2, 1]
        
        '''
        
        while self.q1:
            tmp.append(self.q1.pop(0))
            
        self.q1 = tmp
        

    def pop(self) -> int:
        return self.q1.pop(0)
        

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()





class MyStack:
    '''
    03082022, push O(1), pop O(n)
    '''
    def __init__(self):
        self.q1 = []
        

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        tmp = []
        if self.empty():
            return None
        
        while len(self.q1) > 1:
            tmp.append(self.q1.pop(0))
            
        res = self.q1.pop(0)
        self.q1 = tmp

        return res
        

    def top(self) -> int:
        tmp = []
        if self.empty():
            return None
        
        while len(self.q1) > 1:
            tmp.append(self.q1.pop(0))
            
        top = self.q1[0]
        tmp.append(top)
        self.q1 = tmp
        
        return top
            
    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()